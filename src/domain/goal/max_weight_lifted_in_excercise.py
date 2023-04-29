from abc import abstractmethod
from datetime import datetime
from src.domain.goal.goal import Goal

from src.domain.metric.metric import ExcerciseSetCompleted, Metric


class MaxWeightLiftedInExcercise(Goal):
    """A goal that represents the max weight lifted in an excercise."""
    def __init__(
        self,
        goal_weight_in_kg: float,
        excercise_title: str,
        deadline: datetime,
        username: str,
        metrics: list[Metric]
    ):
        if not all(
            isinstance(metric, ExcerciseSetCompleted) for metric in metrics
        ):
            raise ValueError("Metrics must be of type ExcerciseSetCompleted")

        if not all(
            metric.excercise_title == excercise_title for metric in
            metrics
        ):
            raise ValueError("Metrics must be of of the same excercise")

        if not all(
            metric.crated_at < deadline for metric in
            metrics
        ):
            raise ValueError("Metrics must be from before the deadline")

        self._goal_weight_in_kg = goal_weight_in_kg
        self._excercise_title = excercise_title
        self._deadline = deadline
        self._metrics = metrics
        self._username = username

    def _max_weight_lifted_in_kg(self) -> float:
        """The max weight lifted in kg."""
        return max([metric.weight_in_kg for metric in self._metrics])

    def was_achieved(self) -> bool:
        """Returns True if the goal has been achieved."""
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
        return self._deadline < datetime.now() and not self.was_achieved()

    def deadline(self) -> datetime:
        """The deadline of the goal."""
        return self._deadline

    @abstractmethod
    def goal_value(self) -> float:
        """The goal value to be achieved."""
        return self._goal_weight_in_kg

    @abstractmethod
    def metrics(self) -> list[Metric]:
        """The metrics that are used to measure the goal progress."""
        return self._metrics
