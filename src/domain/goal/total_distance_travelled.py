from datetime import datetime
from src.domain.goal.goal import Goal
from src.domain.metric.metric import DistanceTravelled, Metric, StepsTaken


class TotalDistanceTravelled(Goal):
    """A goal that represents the distance tavelled in a time interval."""

    def __init__(self, goal_dict: dict, metric_factory):
        """Initializes the goal with a dict."""
        super().__init__(goal_dict, metric_factory)
        self._goal_distance_in_meters = goal_dict["goal_distance_in_meters"]

    def goal_value(self) -> float:
        """The goal value to be completed."""
        return self._goal_distance_in_meters

    def current_value(self) -> float:
        """The current value of the goal."""
        distances = [metric.distance_in_meters for metric in self._metrics]
        return sum(distances) if distances else 0
