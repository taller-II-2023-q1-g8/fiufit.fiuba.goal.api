from datetime import datetime
from dataclasses import dataclass


@dataclass
class Metric:
    created_at: datetime
    username: str


@dataclass
class TrainingPlanCompleted(Metric):
    """A metric that represents the completion of a training plan."""
    plan_title: str


@dataclass
class ExcerciseSetCompleted(Metric):
    """A metric that represents the completion of an excercise"""
    excercise_title: str
    weight_in_kg: float
    reps: int


@dataclass
class WeightMeasured(Metric):
    """A metric that represents the user's weight measured"""
    weight: float


@dataclass
class DistanceTravelled(Metric):
    """A metric that represents a walk."""
    distance: float
    duration: float

    def pace(self):
        return self.distance / self.duration


@dataclass
class CaloriesBurned(Metric):
    """A metric that represents the calories burned by the user"""
    calories: float
