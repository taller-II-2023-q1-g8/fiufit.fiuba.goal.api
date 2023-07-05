from datetime import datetime
from src.domain.goal.goal import Goal
from src.domain.metric.metric import Metric, StepsTaken


class TotalStepsTaken(Goal):
    """A goal that represents the number of steps taken in a time interval."""

    def __init__(self, goal_dict: dict, metric_factory):
        """Initializes the goal with a dict."""
        super().__init__(goal_dict, metric_factory)
        self._goal_num_of_steps = goal_dict["goal_num_of_steps"]

    def goal_value(self) -> float:
        """The goal value to be completed."""
        return self._goal_num_of_steps

    def current_value(self) -> float:
        """The current value of the goal."""
        steps_taken = [metric.step_count for metric in self._metrics]
        return sum(steps_taken) if steps_taken else 0
