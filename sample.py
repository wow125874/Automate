import os
import asyncio
import time
import re
from dotenv import load_dotenv
import google.generativeai as genai
from playwright.async_api import async_playwright

# Load .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# === Gemini Prompt + Code Generation ===
def generate_code_from_prompt(prompt, screenshot_path=None):
    system_prompt = """
You are an expert in generating Playwright Python code.
Return only the code that would go inside an async function that takes `page` as its argument.

Only output Playwright commands like:
- await page.goto(...)
- await page.fill(...)
- await page.click(...)
- etc.

Do NOT wrap in `async def run(page):`
Do NOT include any explanations or markdown. Just return the raw lines.
"""

    if screenshot_path:
        prompt += f"\nThere was an error in the original automation. Here is a screenshot for context: {screenshot_path}\nFix the code."

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(system_prompt + "\nUser Request:\n" + prompt)

    code = response.text.strip()
    code = re.sub(r"```(?:python)?", "", code)
    code = code.replace("```", "").strip()

    if not code.startswith("async def run(page):"):
        code = "async def run(page):\n" + "\n".join("    " + line for line in code.splitlines())

    return code

# === Playwright Execution of Generated Code ===
async def run_automation(code: str, prompt: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        exec_env = {
            "page": page,
            "asyncio": asyncio,
            "time": time
        }

        try:
            print("\n🚀 Running browser automation...\n")
            exec(code, exec_env)
            await exec_env["run"](page)
            print("\n✅ Automation complete.")
        except Exception as e:
            print("\n❌ Error running code:", e)
            screenshot_path = "error_screenshot.png"
            await page.screenshot(path=screenshot_path)
            print(f"📸 Screenshot saved to {screenshot_path}")

            retry = input("\n🔁 Retry with updated Gemini code? (y/n): ").strip().lower()
            if retry == "y":
                new_code = generate_code_from_prompt(prompt, screenshot_path=screenshot_path)
                print("\n=== Retrying with Updated Code ===\n")
                print(new_code)
                await run_automation(new_code, prompt)
        finally:
            input("\nPress Enter to close the browser...")
            await browser.close()

# === Main Flow ===
def main():
    user_prompt = input("🧠 What do you want the browser to do?\n> ")
    code = generate_code_from_prompt(user_prompt)
    code = code.replace('fill("input[name', 'fill("textarea[name')

    if "pass" in code or len(code) < 30:
        print("⚠️ Gemini returned empty or non-functional code.")
        return

    print("\n=== Generated Code ===\n")
    print(code)

    if input("\n▶️ Run this in browser? (y/n): ").strip().lower() == "y":
        asyncio.run(run_automation(code, user_prompt))
    else:
        print("❌ Cancelled.")

if __name__ == "__main__":
    main()
