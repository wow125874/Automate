# High-Level Design - Lateral Hire Onboarding Application

## 1. System Overview

The Lateral Hire Onboarding Application is designed to provide personalized learning journeys for lateral hires based on their service line and experience level. The system automates task verification using external APIs and enhances user experience through AI-powered assistance.

## 2. Current Implementation Status

### 2.1 Development Progress
- **Frontend**: Angular application fully implemented with routing, components, and services
- **Backend**: .NET Core API with complete service layer and controllers implemented
- **Database**: In-memory repositories implemented for development, SQL schema ready for production
- **Authentication**: JWT token integration structure in place
- **AI Integration**: ChatBot service interface implemented, Azure OpenAI integration ready

### 2.2 Implemented Services
- **User Management**: Complete CRUD operations with UserService and UsersController
- **Journey Management**: Journey creation, assignment, and tracking via JourneyService
- **Content Management**: Content CRUD operations with ContentService and ContentsController
- **Task Management**: Task creation, assignment, and verification via TaskService
- **User Task Tracking**: UserTaskService with status tracking and completion workflows
- **ChatBot Integration**: ChatBotService with session management and knowledge base
- **Notification System**: NotificationService for reminders and deadline notifications
- **Scoring System**: ScoringService for points and score calculations

### 2.3 Recent Fixes and Improvements
- **ILogger Integration**: Fixed missing using directives in ContentFactory.cs and EventPublisher.cs
- **Task Ambiguity**: Resolved System.Threading.Tasks.Task vs Core.Models.Task conflicts
- **Repository Interfaces**: Implemented missing methods in service interfaces
- **Service Registration**: Complete dependency injection setup in Program.cs
- **Controller Implementation**: All major controllers implemented with proper error handling

## 3. Architecture Overview

![High-Level Architecture](./images/high-level-architecture.png)

The application follows a microservices-based architecture with the following key components:

### 2.1 Frontend Layer
- **Angular SPA**: Single-page application providing responsive UI for both users and administrators
- **UI Components**: Reusable components for dashboards, learning journeys, and admin configurations
- **State Management**: NgRx for state management across the application

### 2.2 API Gateway Layer
- **API Gateway**: Azure API Management service for routing, authentication, and API composition
- **Authentication/Authorization**: Azure AD B2C integration for secure user authentication

### 2.2 Implemented Services Architecture

#### 2.2.1 Core API Services (LateralHireOnboarding.API)

1. **User Management**
   - **Controller**: UsersController with full CRUD operations
   - **Service**: UserService implementing IUserService interface
   - **Repository**: InMemoryUserRepository for development
   - **Features**: User registration, profile management, authentication support

2. **Journey Management**
   - **Controller**: JourneysController for journey operations
   - **Service**: JourneyService with journey creation and assignment
   - **Repository**: InMemoryJourneyRepository
   - **Features**: Journey templates, personalized path creation, service line mapping

3. **Content Management**
   - **Controller**: ContentsController with content CRUD
   - **Service**: ContentService implementing IContentService
   - **Repository**: InMemoryContentRepository and InMemoryJourneyContentRepository
   - **Features**: Content creation, type-based filtering, journey assignment

4. **Task Management**
   - **Controller**: TasksController for task operations
   - **Service**: TaskService and UserTaskService
   - **Repository**: InMemoryTaskRepository and InMemoryUserTaskRepository
   - **Features**: Task creation, assignment, status tracking, completion workflows

5. **ChatBot Integration**
   - **Controller**: ChatBotController for AI interactions
   - **Service**: ChatBotService with session management
   - **Repository**: InMemoryChatSessionRepository, InMemoryChatMessageRepository, InMemoryKnowledgeItemRepository
   - **Features**: Chat sessions, knowledge base search, AI response processing

6. **Notification System**
   - **Controller**: NotificationsController
   - **Service**: NotificationService implementing INotificationService
   - **Features**: Reminder notifications, deadline alerts, bulk messaging

7. **Scoring System**
   - **Controller**: ScoringController
   - **Service**: ScoringService implementing IScoringService
   - **Features**: Points calculation, score tracking, journey completion metrics

#### 2.2.2 Specialized Microservices

1. **Task Verification Service** (Separate microservice)
   - External API integration (GitHub, Jira, Slack)
   - Strategy pattern implementation for different verification types
   - Circuit breaker and retry policies for resilience

2. **AI Assistant Service** (Separate microservice)
   - Azure OpenAI integration ready
   - Document processing capabilities
   - Personalized recommendation engine

### 2.3 Data Layer Implementation
- **Development**: In-memory repositories for rapid development and testing
- **Production Ready**: Azure SQL Database schema designed and ready for deployment
- **Storage**: Azure Blob Storage integration planned for learning materials
- **AI Data**: Cosmos DB schema ready for AI interaction logs

### 2.4 Current Technology Stack
- **Backend**: .NET 7 with Entity Framework Core
- **Frontend**: Angular 16 with TypeScript
- **Development Database**: In-memory repositories with full CRUD operations
- **Production Database**: SQL Server with Entity Framework migrations ready
- **API Documentation**: Swagger/OpenAPI integration
- **Dependency Injection**: Complete service registration and interface implementation
- **Logging**: ILogger integration throughout the application
- **Error Handling**: Comprehensive exception handling in controllers and services

### 2.6 Integration Layer
- **External API Connectors**: For integrating with external systems for task verification
- **Event Bus**: Azure Service Bus for asynchronous communication between services
- **Notification Service**: For sending emails, chat messages, and nudges

## 3. Cross-Cutting Concerns

### 3.1 Security
- **Authentication**: Azure AD B2C for identity management
- **Authorization**: Role-based access control (RBAC) for different user types
- **Data Protection**: Encryption at rest and in transit
- **Audit Logging**: Comprehensive logging of all system activities

### 3.2 Scalability
- **Horizontal Scaling**: Ability to scale individual microservices based on demand
- **Auto-scaling**: Azure App Service auto-scaling for handling varying loads
- **Load Balancing**: Azure Load Balancer for distributing traffic

### 3.3 Monitoring and Logging
- **Application Insights**: For monitoring application performance
- **Log Analytics**: For centralized logging and analysis
- **Health Checks**: Regular health checks for all services

### 3.4 DevOps
- **CI/CD Pipeline**: Azure DevOps for continuous integration and deployment
- **Infrastructure as Code**: Azure Resource Manager templates for infrastructure provisioning
- **Containerization**: Docker containers for consistent deployment environments

## 4. Key Design Decisions

### 4.1 Microservices Architecture
The application uses a microservices architecture to ensure:
- **Modularity**: Each service has a specific responsibility
- **Scalability**: Services can be scaled independently based on demand
- **Maintainability**: Services can be developed, tested, and deployed independently
- **Technology Flexibility**: Different services can use different technologies if needed

### 4.2 CQRS Pattern
Command Query Responsibility Segregation (CQRS) pattern is used for:
- **Separation of Concerns**: Read and write operations are separated
- **Performance Optimization**: Read and write models can be optimized independently
- **Scalability**: Read and write operations can be scaled independently

### 4.3 Repository Pattern
Repository pattern is used for data access to:
- **Abstract Data Access**: Hide the details of data access from the business logic
- **Testability**: Make it easier to test business logic by mocking repositories
- **Maintainability**: Centralize data access logic

### 4.4 Factory Pattern
Factory pattern is used for creating complex objects:
- **Learning Path Factory**: For creating personalized learning paths based on service line and experience level
- **Content Factory**: For creating different types of content (video, document, link)

### 4.5 Observer Pattern
Observer pattern is used for event handling:
- **Task Completion Events**: Notify interested parties when a task is completed
- **Progress Tracking**: Update progress when a module or course is completed

## 5. System Interactions

### 5.1 User Onboarding Flow
1. User logs in using Azure AD B2C
2. User profile is created/retrieved
3. Learning path is automatically generated based on service line and experience level
4. Personalized dashboard is displayed with assigned journey

### 5.2 Learning Journey Flow
1. User navigates through courses, modules, and topics
2. User consumes content (videos, documents, links)
3. User completes tasks
4. Task verification service verifies task completion using external APIs
5. Progress is updated automatically

### 5.3 AI Assistant Interaction Flow
1. User interacts with AI assistant for queries
2. AI assistant processes the query using Azure OpenAI
3. AI assistant provides responses, summarizes documents, or helps with task verification
4. Interactions are logged for future reference and improvement

### 5.4 Admin Configuration Flow
1. Admin logs in with admin privileges
2. Admin configures master data (service lines, experience levels, courses, etc.)
3. Admin defines journey templates with duration, modules, and timelines
4. Admin views reports and analytics on user progress and system usage

## 6. Deployment Architecture

![Deployment Architecture](./images/deployment-architecture.png)

The application will be deployed on Azure with the following components:

- **Azure App Service**: For hosting the Angular SPA and API services
- **Azure SQL Database**: For relational data storage
- **Azure Blob Storage**: For content storage
- **Azure Cosmos DB**: For unstructured data storage
- **Azure OpenAI Service**: For AI capabilities
- **Azure Functions**: For serverless processing
- **Azure Service Bus**: For asynchronous messaging
- **Azure API Management**: For API gateway
- **Azure AD B2C**: For identity management
- **Azure Application Insights**: For monitoring and logging
- **Azure DevOps**: For CI/CD pipeline

## 7. Conclusion

The high-level design provides a comprehensive architecture for the Lateral Hire Onboarding Application. The microservices-based approach ensures modularity, scalability, and maintainability, while the integration with Azure services provides robust cloud capabilities. The AI integration enhances the user experience with intelligent assistance and automation.