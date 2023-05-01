from datetime import datetime
from src.domain.goal.goal import Goal

from src.domain.metric.metric import ExerciseSetCompleted, Metric


class MaxWeightLiftedInExercise(Goal):
    """A goal that represents the max weight lifted in an excercise."""

    def __init__(self, goal_dict: dict, metric_factory):
        """Initializes the goal with a dict."""

        self.id = goal_dict["_id"]
        self._goal_weight_in_kg = goal_dict["goal_weight_in_kg"]
        self._exercise_title = goal_dict["exercise_title"]
        self._username = goal_dict["username"]
        self._starting_date = goal_dict["starting_date"]
        self._deadline = goal_dict["deadline"]
        self._metrics = [
            metric_factory.from_dict(metric_dict) for
            metric_dict in goal_dict["metrics"]
        ]

    def _max_weight_lifted_in_kg(self) -> float:
        """The max weight lifted in kg."""
        weights_lifted = [metric.weight_in_kg for metric in self._metrics]
        return max(weights_lifted) if weights_lifted else 0

    def was_completed(self) -> bool:
        """Returns True if the goal has been completed."""
        return self._max_weight_lifted_in_kg() >= self._goal_weight_in_kg

    def completion_percentage(self) -> float:
        """The percentage of the goal completion."""

        completion_fraction = min(
            1.0,
            self._max_weight_lifted_in_kg()/self._goal_weight_in_kg
        )

        return 100 * completion_fraction

    def was_failed(self) -> bool:
        """Returns True if the deadline has passed."""
        return self._deadline < datetime.now() and not self.was_completed()

    def starting_date(self) -> datetime:
        """The starting date of the goal."""
        return self._starting_date

    def deadline(self) -> datetime:
        """The deadline of the goal."""
        return self._deadline

    def goal_value(self) -> float:
        """The goal value to be completed."""
        return self._goal_weight_in_kg

    def add_metrics(self, metrics: list[Metric]):
        """Adds new metrics to the goal."""
        new_metrics = list(filter(
            lambda metric:
                isinstance(metric, ExerciseSetCompleted) and
                metric.exercise_title == self._exercise_title and
                metric.created_at > self._starting_date and
                metric.created_at < self._deadline,
                metrics
        ))

        self._metrics.extend(new_metrics)

    def metrics(self) -> list[Metric]:
        """The metrics that are used to measure the goal progress."""
        return self._metrics

    def exercise_title(self) -> str:
        """The excercise title of the goal."""
        return self._exercise_title
    
    def to_dict(self) -> dict:
        """Returns a dict representation of the goal."""
        return {
            "id": self.id,
            "goal_weight_in_kg": self._goal_weight_in_kg,
            "exercise_title": self._exercise_title,
            "starting_date": self._starting_date,
            "deadline": self._deadline,
            "metrics": self._metrics
        }