from datetime import datetime
from dataclasses import dataclass


@dataclass
class Metric:
    created_at: datetime


@dataclass
class TrainingPlanCompleted(Metric):
    """A metric that represents the completion of a training plan."""

    plan_title: str

    def __init__(self, goal_dict: dict):
        """Initializes the metric with a dict."""
        self.created_at = goal_dict["created_at"]
        self.plan_title = goal_dict["plan_title"]


@dataclass
class ExerciseSetCompleted(Metric):
    """A metric that represents the completion of an excercise"""

    exercise_title: str
    weight_in_kg: float
    reps: int

    def __init__(self, goal_dict: dict):
        """Initializes the metric with a dict."""
        self.created_at = goal_dict["created_at"]
        self.exercise_title = goal_dict["exercise_title"]
        self.weight_in_kg = goal_dict["weight_in_kg"]
        self.reps = goal_dict["reps"]


@dataclass
class WeightMeasured(Metric):
    """A metric that represents the user's weight measured"""

    weight_in_kg: float

    def __init__(self, goal_dict: dict):
        """Initializes the metric with a dict."""
        self.created_at = goal_dict["created_at"]
        self.weight_in_kg = goal_dict["weight_in_kg"]


@dataclass
class DistanceTravelled(Metric):
    """A metric that represents a walk."""

    distance_in_km: float
    duration_in_min: float

    def __init__(self, goal_dict: dict):
        """Initializes the metric with a dict."""
        self.created_at = goal_dict["created_at"]
        self.distance_in_km = goal_dict["distance_in_km"]
        self.duration_in_min = goal_dict["duration_in_min"]


@dataclass
class CaloriesBurned(Metric):
    """A metric that represents the calories burned by the user"""

    calories: float

    def __init__(self, goal_dict: dict):
        """Initializes the metric with a dict."""
        self.created_at = goal_dict["created_at"]
        self.calories = goal_dict["calories"]


# class MetricFactory:
#     """A factory that creates metrics."""

#     def create_metric(self, metric_dict: dict) -> Metric:
#         """Creates a metric from a dict."""
#         match metric_dict['type']:
#             case 'training_plan_completed':
#                 return TrainingPlanCompleted(metric_dict)
#             case 'exercise_set_completed':
#                 return ExcerciseSetCompleted(metric_dict)
#             case 'weight_measured':
#                 return WeightMeasured(metric_dict)
#             case 'distance_travelled':
#                 return DistanceTravelled(metric_dict)
#             case 'calories_burned':
#                 return CaloriesBurned(metric_dict)
