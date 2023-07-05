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
    """A metric that represents the completion of an exercise"""

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
class StepsTaken(Metric):
    """A metric that represents the steps taken during a time interval"""

    step_count: int
    duration_in_seconds: float

    def __init__(self, goal_dict: dict):
        """Initializes the metric with a dict."""
        self.created_at = goal_dict["created_at"]
        self.duration_in_seconds = goal_dict["duration_in_seconds"]
        self.step_count = goal_dict["step_count"]


@dataclass
class DistanceTravelled(Metric):
    """A metric that represents a walk."""

    distance_in_meters: float
    duration_in_seconds: float

    def __init__(self, goal_dict: dict):
        """Initializes the metric with a dict."""
        self.created_at = goal_dict["created_at"]
        self.distance_in_meters = goal_dict["distance_in_meters"]
        self.duration_in_seconds = goal_dict["duration_in_seconds"]


# @dataclass
# class WeightMeasured(Metric):
#     """A metric that represents the user's weight measured"""

#     weight_in_kg: float

#     def __init__(self, goal_dict: dict):
#         """Initializes the metric with a dict."""
#         self.created_at = goal_dict["created_at"]
#         self.weight_in_kg = goal_dict["weight_in_kg"]

# @dataclass
# class CaloriesBurned(Metric):
#     """A metric that represents the calories burned by the user"""

#     calories: float

#     def __init__(self, goal_dict: dict):
#         """Initializes the metric with a dict."""
#         self.created_at = goal_dict["created_at"]
#         self.calories = goal_dict["calories"]
