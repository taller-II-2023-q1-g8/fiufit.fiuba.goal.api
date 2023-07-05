from datetime import datetime
from src.domain.goal.goal import Goal

from src.domain.metric.metric import ExerciseSetCompleted, Metric


class MaxWeightLiftedInExercise(Goal):
    """A goal that represents the max weight lifted in an exercise."""

    def __init__(self, goal_dict: dict, metric_factory):
        """Initializes the goal with a dict."""
        super().__init__(goal_dict, metric_factory)
        self._goal_weight_in_kg = goal_dict["goal_weight_in_kg"]
        self._exercise_title = goal_dict["exercise_title"]

    def current_value(self) -> float:
        """The max weight lifted in kg."""
        weights_lifted = [metric.weight_in_kg for metric in self._metrics]
        return max(weights_lifted) if weights_lifted else 0

    def goal_value(self) -> float:
        """The goal value to be completed."""
        return self._goal_weight_in_kg