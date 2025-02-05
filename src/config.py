"""Setup the application's configuration."""
from src.infrastructure.goal.goal_factory import GoalFactory
from src.infrastructure.goal.goal_query import GoalQuery
from src.infrastructure.goal.goal_repository_mongodb import GoalRepositoryMongoDB
from src.infrastructure.notification.notification_repository_mongodb import NotificationRepositoryMongoDB
from src.infrastructure.metric.metric_factory import MetricFactory
from src.infrastructure.metric.metric_query import MetricsQuery
from src.infrastructure.metric.metric_repository_mongodb import MetricRepositoryMongoDB
from src.usecase.goals_service import GoalService
from src.usecase.metrics_service import MetricService
from src.infrastructure.mongodb_connection import metrics_collection, goals_collection, notifications_collection
from src.infrastructure.notification.notification_service import NotificationService

# Metrics Factory
metrics_factory = MetricFactory()

# Metrics Repository
metrics_repository = MetricRepositoryMongoDB(metrics_collection)

# Metrics Query Module
metrics_query_module = MetricsQuery(metrics_collection)

# Goals Factory
goal_factory = GoalFactory(metrics_factory)

# Goals Repository
goals_repository = GoalRepositoryMongoDB(
    goals_collection, metrics_query_module, metrics_factory
)

# Goals Query Module
goals_query_module = GoalQuery(goals_collection, goal_factory, metrics_query_module)

# Notification Repository
# notification_repository = NotificationRepositoryMongoDB(notifications_collection)

# Notification Service
notification_service = NotificationService(goals_repository)

# Goals Application Service
goals_service = GoalService(goals_repository, goals_query_module, goal_factory) #, notification_repository)

# Metrics Application Service
metrics_service = MetricService(metrics_repository, metrics_query_module, goals_query_module, notification_service)