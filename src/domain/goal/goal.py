from abc import abstractmethod
from datetime import datetime

from src.domain.metric.metric import Metric


class Goal:
    id: str

    @abstractmethod
    def was_completed(self) -> bool:
        """Returns True if the goal has been completed."""
        raise NotImplementedError

    def in_progress(self) -> bool:
        """Returns True if the goal is in progress."""
        return not self.was_completed() and not self.was_failed()

    @abstractmethod
    def completion_percentage(self) -> float:
        """The percentage of the goal completion."""
        raise NotImplementedError

    @abstractmethod
    def was_failed(self) -> bool:
        """Returns True if the deadline has passed."""
        raise NotImplementedError

    @abstractmethod
    def starting_date(self) -> datetime:
        """The starting date of the goal."""
        raise NotImplementedError

    @abstractmethod
    def deadline(self) -> datetime:
        """The deadline of the goal."""
        raise NotImplementedError

    @abstractmethod
    def goal_value(self) -> float:
        """The goal value to be completed."""
        raise NotImplementedError

    @abstractmethod
    def add_metrics(self, metric: list[Metric]):
        """Adds a metric to the goal."""
        raise NotImplementedError

    @abstractmethod
    def metrics(self) -> list[Metric]:
        """The metrics that are used to measure the goal progress."""
        raise NotImplementedError
