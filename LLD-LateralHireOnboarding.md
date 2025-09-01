# Low-Level Design - Lateral Hire Onboarding Application

## 1. Component Design

### 1.1 Frontend Components

#### 1.1.1 Angular Module Structure

```
src/app/
├── core/                  # Core functionality used throughout the application
│   ├── authentication/    # Authentication services and guards
│   ├── http/              # HTTP interceptors and services
│   ├── models/            # Core data models
│   └── services/          # Core services
├── features/              # Feature modules
│   ├── admin/             # Admin features
│   │   ├── configuration/ # Master data configuration
│   │   ├── reporting/     # Reporting and analytics
│   │   └── templates/     # Journey templates
│   ├── learning/          # Learning journey features
│   │   ├── courses/       # Course components
│   │   ├── modules/       # Module components
│   │   └── topics/        # Topic components
│   ├── onboarding/        # User onboarding features
│   │   ├── profile/       # User profile components
│   │   └── dashboard/     # User dashboard components
│   └── ai-assistant/      # AI assistant features
│       ├── chatbot/       # FAQ chatbot components
│       ├── summarization/ # Document summarization components
│       └── nudges/        # Progress nudge components
├── shared/                # Shared components, directives, and pipes
│   ├── components/        # Reusable UI components
│   ├── directives/        # Custom directives
│   └── pipes/             # Custom pipes
└── app.module.ts          # Main application module
```

#### 1.1.2 State Management (NgRx)

```
src/app/store/
├── actions/               # Action creators
│   ├── user.actions.ts
│   ├── learning.actions.ts
│   ├── admin.actions.ts
│   └── ai.actions.ts
├── effects/               # Side effects
│   ├── user.effects.ts
│   ├── learning.effects.ts
│   ├── admin.effects.ts
│   └── ai.effects.ts
├── reducers/              # State reducers
│   ├── user.reducer.ts
│   ├── learning.reducer.ts
│   ├── admin.reducer.ts
│   └── ai.reducer.ts
├── selectors/             # State selectors
│   ├── user.selectors.ts
│   ├── learning.selectors.ts
│   ├── admin.selectors.ts
│   └── ai.selectors.ts
└── index.ts               # Root state
```

#### 1.1.3 Key UI Components

- **UserDashboardComponent**: Displays personalized dashboard with assigned journey
- **CourseNavigatorComponent**: Provides navigation through courses, modules, and topics
- **ContentViewerComponent**: Displays different types of content (video, document, link)
- **TaskVerificationComponent**: Handles task verification and displays status
- **AIChatbotComponent**: Provides interface for interacting with AI assistant
- **AdminConfigurationComponent**: Provides interface for configuring master data and templates
- **ReportingDashboardComponent**: Displays reports and analytics

### 1.2 Backend Services

#### 1.2.1 Microservice Structure

Each microservice follows a similar structure:

```
ServiceName/
├── ServiceName.API/                # API layer
│   ├── Controllers/                # API controllers
│   ├── Middleware/                 # Custom middleware
│   ├── Filters/                    # Action filters
│   └── Program.cs                  # Application entry point
├── ServiceName.Application/        # Application layer
│   ├── Commands/                   # Command handlers (CQRS)
│   ├── Queries/                    # Query handlers (CQRS)
│   ├── DTOs/                       # Data transfer objects
│   ├── Mappings/                   # AutoMapper profiles
│   └── Behaviors/                  # Pipeline behaviors
├── ServiceName.Domain/             # Domain layer
│   ├── Entities/                   # Domain entities
│   ├── ValueObjects/               # Value objects
│   ├── Enums/                      # Enumerations
│   ├── Events/                     # Domain events
│   └── Exceptions/                 # Domain exceptions
├── ServiceName.Infrastructure/     # Infrastructure layer
│   ├── Persistence/                # Data access
│   │   ├── Repositories/           # Repository implementations
│   │   ├── Configurations/         # Entity configurations
│   │   └── Context/                # DbContext
│   ├── Services/                   # External service implementations
│   ├── Logging/                    # Logging infrastructure
│   └── Identity/                   # Identity infrastructure
└── ServiceName.Tests/              # Tests
    ├── Unit/                       # Unit tests
    ├── Integration/                # Integration tests
    └── Functional/                 # Functional tests
```

#### 1.2.2 User Management Service

**Key Components:**
- **UserController**: API endpoints for user management
- **UserProfileEntity**: Domain entity for user profiles
- **UserRepository**: Repository for user data access
- **AuthenticationService**: Service for authentication and authorization

**Key APIs:**
- `POST /api/users`: Create a new user
- `GET /api/users/{id}`: Get user by ID
- `PUT /api/users/{id}`: Update user profile
- `GET /api/users/{id}/journey`: Get user's learning journey

#### 1.2.3 Learning Journey Service

**Key Components:**
- **CourseController**: API endpoints for courses
- **ModuleController**: API endpoints for modules
- **TopicController**: API endpoints for topics
- **LearningPathFactory**: Factory for creating personalized learning paths
- **CourseEntity**, **ModuleEntity**, **TopicEntity**: Domain entities

**Key APIs:**
- `GET /api/courses`: Get all courses
- `GET /api/courses/{id}`: Get course by ID
- `GET /api/courses/{id}/modules`: Get modules for a course
- `GET /api/modules/{id}/topics`: Get topics for a module
- `GET /api/topics/{id}/content`: Get content for a topic

#### 1.2.4 Task Verification Service

**Key Components:**
- **TaskController**: API endpoints for tasks
- **ExternalApiClient**: Client for external API integration
- **TaskVerificationService**: Service for verifying task completion
- **TaskEntity**: Domain entity for tasks

**Key APIs:**
- `GET /api/tasks`: Get all tasks
- `GET /api/tasks/{id}`: Get task by ID
- `POST /api/tasks/{id}/verify`: Verify task completion
- `GET /api/users/{id}/tasks`: Get tasks for a user

#### 1.2.5 AI Assistant Service

**Key Components:**
- **ChatbotController**: API endpoints for chatbot
- **SummarizationController**: API endpoints for document summarization
- **NudgeController**: API endpoints for progress nudges
- **OpenAIService**: Service for interacting with Azure OpenAI
- **InteractionLogEntity**: Domain entity for AI interactions

**Key APIs:**
- `POST /api/chatbot/query`: Submit a query to the chatbot
- `POST /api/summarization/document`: Summarize a document
- `POST /api/nudges/send`: Send a progress nudge
- `GET /api/users/{id}/interactions`: Get AI interactions for a user

#### 1.2.6 Admin Configuration Service

**Key Components:**
- **ServiceLineController**: API endpoints for service lines
- **ExperienceLevelController**: API endpoints for experience levels
- **JourneyTemplateController**: API endpoints for journey templates
- **ConfigurationEntity**: Domain entity for configurations

**Key APIs:**
- `GET /api/servicelines`: Get all service lines
- `POST /api/servicelines`: Create a new service line
- `GET /api/experiencelevels`: Get all experience levels
- `POST /api/experiencelevels`: Create a new experience level
- `GET /api/journeytemplates`: Get all journey templates
- `POST /api/journeytemplates`: Create a new journey template

#### 1.2.7 Reporting Service

**Key Components:**
- **ReportController**: API endpoints for reports
- **AnalyticsService**: Service for generating analytics
- **ReportEntity**: Domain entity for reports

**Key APIs:**
- `GET /api/reports/progress`: Get progress reports
- `GET /api/reports/completion`: Get completion rate reports
- `GET /api/reports/ai-activity`: Get AI activity reports
- `GET /api/reports/feedback`: Get feedback reports

### 1.3 Data Models

#### 1.3.1 User Management

```csharp
public class User
{
    public Guid Id { get; set; }
    public string Email { get; set; }
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public DateTime JoinDate { get; set; }
    public Guid ServiceLineId { get; set; }
    public ServiceLine ServiceLine { get; set; }
    public Guid ExperienceLevelId { get; set; }
    public ExperienceLevel ExperienceLevel { get; set; }
    public Guid LearningPathId { get; set; }
    public LearningPath LearningPath { get; set; }
    public List<UserTask> Tasks { get; set; }
    public List<AIInteraction> AIInteractions { get; set; }
}

public class ServiceLine
{
    public Guid Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public List<User> Users { get; set; }
    public List<JourneyTemplate> JourneyTemplates { get; set; }
}

public class ExperienceLevel
{
    public Guid Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public int Level { get; set; }
    public List<User> Users { get; set; }
    public List<JourneyTemplate> JourneyTemplates { get; set; }
}
```

#### 1.3.2 Learning Journey

```csharp
public class LearningPath
{
    public Guid Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
    public Guid JourneyTemplateId { get; set; }
    public JourneyTemplate JourneyTemplate { get; set; }
    public Guid UserId { get; set; }
    public User User { get; set; }
    public List<CourseAssignment> CourseAssignments { get; set; }
}

public class JourneyTemplate
{
    public Guid Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public int DurationInDays { get; set; }
    public Guid ServiceLineId { get; set; }
    public ServiceLine ServiceLine { get; set; }
    public Guid ExperienceLevelId { get; set; }
    public ExperienceLevel ExperienceLevel { get; set; }
    public List<CourseTemplate> CourseTemplates { get; set; }
    public List<LearningPath> LearningPaths { get; set; }
}

public class Course
{
    public Guid Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public int Order { get; set; }
    public List<Module> Modules { get; set; }
    public List<CourseAssignment> CourseAssignments { get; set; }
    public List<CourseTemplate> CourseTemplates { get; set; }
}

public class CourseTemplate
{
    public Guid Id { get; set; }
    public Guid CourseId { get; set; }
    public Course Course { get; set; }
    public Guid JourneyTemplateId { get; set; }
    public JourneyTemplate JourneyTemplate { get; set; }
    public int Order { get; set; }
    public int DurationInDays { get; set; }
}

public class CourseAssignment
{
    public Guid Id { get; set; }
    public Guid CourseId { get; set; }
    public Course Course { get; set; }
    public Guid LearningPathId { get; set; }
    public LearningPath LearningPath { get; set; }
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
    public CourseStatus Status { get; set; }
    public int CompletionPercentage { get; set; }
    public List<ModuleAssignment> ModuleAssignments { get; set; }
}

public class Module
{
    public Guid Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public int Order { get; set; }
    public Guid CourseId { get; set; }
    public Course Course { get; set; }
    public List<Topic> Topics { get; set; }
    public List<ModuleAssignment> ModuleAssignments { get; set; }
}

public class ModuleAssignment
{
    public Guid Id { get; set; }
    public Guid ModuleId { get; set; }
    public Module Module { get; set; }
    public Guid CourseAssignmentId { get; set; }
    public CourseAssignment CourseAssignment { get; set; }
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
    public ModuleStatus Status { get; set; }
    public int CompletionPercentage { get; set; }
    public List<TopicAssignment> TopicAssignments { get; set; }
}

public class Topic
{
    public Guid Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public int Order { get; set; }
    public Guid ModuleId { get; set; }
    public Module Module { get; set; }
    public List<Content> Contents { get; set; }
    public List<Task> Tasks { get; set; }
    public List<TopicAssignment> TopicAssignments { get; set; }
}

public class TopicAssignment
{
    public Guid Id { get; set; }
    public Guid TopicId { get; set; }
    public Topic Topic { get; set; }
    public Guid ModuleAssignmentId { get; set; }
    public ModuleAssignment ModuleAssignment { get; set; }
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
    public TopicStatus Status { get; set; }
    public List<UserTask> UserTasks { get; set; }
}
```

#### 1.3.3 Content and Tasks

```csharp
public class Content
{
    public Guid Id { get; set; }
    public string Title { get; set; }
    public string Description { get; set; }
    public ContentType Type { get; set; }
    public string Url { get; set; }
    public string BlobStoragePath { get; set; }
    public int Order { get; set; }
    public Guid TopicId { get; set; }
    public Topic Topic { get; set; }
}

public enum ContentType
{
    Video,
    Document,
    Link
}

public class Task
{
    public Guid Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public string VerificationEndpoint { get; set; }
    public string VerificationMethod { get; set; }
    public string VerificationPayload { get; set; }
    public int Order { get; set; }
    public Guid TopicId { get; set; }
    public Topic Topic { get; set; }
    public List<UserTask> UserTasks { get; set; }
}

public class UserTask
{
    public Guid Id { get; set; }
    public Guid UserId { get; set; }
    public User User { get; set; }
    public Guid TaskId { get; set; }
    public Task Task { get; set; }
    public Guid TopicAssignmentId { get; set; }
    public TopicAssignment TopicAssignment { get; set; }
    public TaskStatus Status { get; set; }
    public DateTime? CompletionDate { get; set; }
    public string VerificationResponse { get; set; }
}

public enum TaskStatus
{
    NotStarted,
    InProgress,
    Completed,
    Failed
}

public enum CourseStatus
{
    NotStarted,
    InProgress,
    Completed
}

public enum ModuleStatus
{
    NotStarted,
    InProgress,
    Completed
}

public enum TopicStatus
{
    NotStarted,
    InProgress,
    Completed
}
```

#### 1.3.4 AI Assistant

```csharp
public class AIInteraction
{
    public Guid Id { get; set; }
    public Guid UserId { get; set; }
    public User User { get; set; }
    public string Query { get; set; }
    public string Response { get; set; }
    public AIInteractionType Type { get; set; }
    public DateTime Timestamp { get; set; }
}

public enum AIInteractionType
{
    Chatbot,
    DocumentSummarization,
    TaskVerification,
    ProgressNudge
}

public class DocumentSummarization
{
    public Guid Id { get; set; }
    public string DocumentUrl { get; set; }
    public string Summary { get; set; }
    public Guid UserId { get; set; }
    public User User { get; set; }
    public DateTime Timestamp { get; set; }
}

public class ProgressNudge
{
    public Guid Id { get; set; }
    public string Message { get; set; }
    public NudgeType Type { get; set; }
    public Guid UserId { get; set; }
    public User User { get; set; }
    public DateTime Timestamp { get; set; }
    public bool Delivered { get; set; }
}

public enum NudgeType
{
    Email,
    Chat,
    Notification
}
```

## 2. Database Design

### 2.1 Azure SQL Database Schema

![Database Schema](./images/database-schema.png)

### 2.2 Azure Blob Storage Structure

```
containers/
├── course-content/           # Course content files
│   ├── videos/               # Video files
│   ├── documents/            # Document files
│   └── images/               # Image files
├── user-uploads/             # User uploaded files
└── ai-interactions/          # AI interaction logs
```

### 2.3 Azure Cosmos DB Collections

- **AIInteractions**: Stores AI interaction logs
- **DocumentSummarizations**: Stores document summarization results
- **ProgressNudges**: Stores progress nudge logs

## 3. API Design

### 3.1 API Gateway Routes

```
/api/
├── users/                    # User Management Service
├── learning/                 # Learning Journey Service
│   ├── courses/              # Course endpoints
│   ├── modules/              # Module endpoints
│   └── topics/               # Topic endpoints
├── tasks/                    # Task Verification Service
├── ai/                       # AI Assistant Service
│   ├── chatbot/              # Chatbot endpoints
│   ├── summarization/        # Document summarization endpoints
│   └── nudges/               # Progress nudge endpoints
├── admin/                    # Admin Configuration Service
│   ├── servicelines/         # Service line endpoints
│   ├── experiencelevels/     # Experience level endpoints
│   └── journeytemplates/     # Journey template endpoints
└── reports/                  # Reporting Service
```

### 3.2 API Authentication and Authorization

- **Authentication**: JWT-based authentication using Azure AD B2C
- **Authorization**: Role-based access control (RBAC) with the following roles:
  - **User**: Regular user with access to learning journey and AI assistant
  - **Admin**: Administrator with access to configuration and reporting
  - **SuperAdmin**: Super administrator with full access to all features

### 3.3 API Versioning

- API versioning is implemented using URL path versioning (e.g., `/api/v1/users`)
- Each API version is maintained separately to ensure backward compatibility

## 4. Integration Design

### 4.1 External API Integration

- **Task Verification APIs**: RESTful APIs for verifying task completion
- **Authentication APIs**: Azure AD B2C APIs for authentication and authorization
- **Notification APIs**: Email and chat APIs for sending notifications

### 4.2 Azure OpenAI Integration

- **Chatbot**: Uses Azure OpenAI for natural language processing and response generation
- **Document Summarization**: Uses Azure OpenAI for summarizing documents
- **Task Verification**: Uses Azure OpenAI for interpreting API responses
- **Progress Nudges**: Uses Azure OpenAI for generating personalized nudges

### 4.3 Event-Driven Integration

- **Azure Service Bus**: Used for asynchronous communication between services
- **Event Grid**: Used for event-driven architecture

## 5. Security Design

### 5.1 Authentication and Authorization

- **Azure AD B2C**: Used for identity management and authentication
- **JWT Tokens**: Used for securing API endpoints
- **Role-Based Access Control**: Used for authorization

### 5.2 Data Protection

- **Encryption at Rest**: All data is encrypted at rest using Azure Storage Service Encryption
- **Encryption in Transit**: All data is encrypted in transit using TLS 1.2 or higher
- **Key Vault**: Used for storing secrets and encryption keys

### 5.3 Audit Logging

- **Application Insights**: Used for logging application events
- **Azure Monitor**: Used for monitoring and alerting
- **Log Analytics**: Used for analyzing logs

## 6. Deployment and DevOps

### 6.1 CI/CD Pipeline

- **Azure DevOps**: Used for continuous integration and deployment
- **Build Pipeline**: Compiles, tests, and packages the application
- **Release Pipeline**: Deploys the application to different environments

### 6.2 Infrastructure as Code

- **Azure Resource Manager (ARM) Templates**: Used for provisioning Azure resources
- **Terraform**: Used for multi-cloud infrastructure provisioning

### 6.3 Containerization

- **Docker**: Used for containerizing the application
- **Azure Container Registry**: Used for storing container images
- **Azure Kubernetes Service**: Used for orchestrating containers

## 7. Testing Strategy

### 7.1 Unit Testing

- **xUnit**: Used for unit testing
- **Moq**: Used for mocking dependencies
- **FluentAssertions**: Used for assertions

### 7.2 Integration Testing

- **TestServer**: Used for in-memory integration testing
- **WebApplicationFactory**: Used for testing the entire application stack

### 7.3 End-to-End Testing

- **Selenium**: Used for browser automation
- **Cypress**: Used for modern web testing

### 7.4 Performance Testing

- **JMeter**: Used for load testing
- **Application Insights**: Used for performance monitoring

## 8. Monitoring and Logging

### 8.1 Application Monitoring

- **Application Insights**: Used for application performance monitoring
- **Azure Monitor**: Used for resource monitoring
- **Health Checks**: Used for service health monitoring

### 8.2 Logging

- **Serilog**: Used for structured logging
- **Log Analytics**: Used for log analysis
- **Application Insights**: Used for telemetry

### 8.3 Alerting

- **Azure Monitor Alerts**: Used for alerting on metrics and logs
- **Action Groups**: Used for notification routing

## 9. Implementation Guidelines

### 9.1 Coding Standards

- **C# Coding Conventions**: Follow Microsoft's C# coding conventions
- **Angular Style Guide**: Follow Angular's style guide
- **RESTful API Design**: Follow RESTful API design principles

### 9.2 Error Handling

- **Global Exception Handling**: Implement global exception handling middleware
- **Structured Error Responses**: Return structured error responses with error codes and messages
- **Logging**: Log all errors with appropriate context

### 9.3 Performance Optimization

- **Caching**: Implement caching for frequently accessed data
- **Pagination**: Implement pagination for large data sets
- **Asynchronous Processing**: Use asynchronous processing for long-running operations

## 10. Conclusion

The low-level design provides a detailed blueprint for implementing the Lateral Hire Onboarding Application. It covers component design, data models, API design, integration design, security design, deployment and DevOps, testing strategy, monitoring and logging, and implementation guidelines. This design ensures that the application meets all functional and non-functional requirements while following best practices for modern cloud-native applications.