from datetime import datetime
from src.domain.goal.goal import Goal
from src.domain.metric.metric import Metric, TrainingPlanCompleted


class TrainingPlanCompletion(Goal):
    """A goal that represents the repeated completion of a training plan."""

    def __init__(self, goal_dict: dict, metric_factory):
        """Initializes the goal with a dict."""
        super().__init__(goal_dict, metric_factory)
        self._goal_num_of_completions = goal_dict["goal_num_of_completions"]

    def current_value(self) -> float:
        """The current value of the goal."""
        return len(self._metrics)

    def goal_value(self) -> float:
        """The goal value to be completed."""
        return self._goal_num_of_completions