from datetime import datetime
from src.domain.goal.goal import Goal
from src.domain.metric.metric import DistanceTravelled, Metric, StepsTaken


class TotalDistanceTravelled(Goal):
    """A goal that represents the distance tavelled in a time interval."""

    def __init__(self, goal_dict: dict, metric_factory):
        """Initializes the goal with a dict."""

        self.id = goal_dict["_id"]
        self._goal_distance_in_meters = goal_dict["goal_distance_in_meters"]
        self._username = goal_dict["username"]
        self._starting_date = goal_dict["starting_date"]
        self._deadline = goal_dict["deadline"]
        self._metrics = [
            metric_factory.from_dict(metric_dict)
            for metric_dict in goal_dict["metrics"]
        ]

    def _distance_travelled(self) -> float:
        """The distance travelled."""
        distances = [metric.distance_in_meters for metric in self._metrics]
        return sum(distances) if distances else 0

    def was_completed(self) -> bool:
        """Returns True if the goal has been completed."""
        return self._distance_travelled() >= self._goal_distance_in_meters

    def completion_percentage(self) -> float:
        """The percentage of the goal completion."""

        completion_fraction = min(
            1.0, self._distance_travelled() / self._goal_distance_in_meters
        )

        return 100 * completion_fraction

    def was_failed(self) -> bool:
        """Returns True if the deadline has passed before the goal was completed."""
        return self._deadline < datetime.now() and not self.was_completed()

    def starting_date(self) -> datetime:
        """The starting date of the goal."""
        return self._starting_date

    def deadline(self) -> datetime:
        """The deadline of the goal."""
        return self._deadline

    def goal_value(self) -> float:
        """The goal value to be completed."""
        return self._goal_distance_in_meters

    def add_metrics(self, metrics: list[Metric]):
        """Adds new metrics to the goal."""
        new_metrics = list(
            filter(
                lambda metric: isinstance(metric, DistanceTravelled)
                and metric.created_at > self._starting_date
                and metric.created_at < self._deadline,
                metrics,
            )
        )

        self._metrics.extend(new_metrics)

    def metrics(self) -> list[Metric]:
        """The metrics of the goal."""
        return self._metrics

    def to_dict(self) -> dict:
        """Returns a dict representation of the goal."""
        return {
            "id": self.id,
            "goal_distance_in_meters": self._goal_distance_in_meters,
            "username": self._username,
            "starting_date": self._starting_date,
            "deadline": self._deadline,
            "metrics": self._metrics,
        }
