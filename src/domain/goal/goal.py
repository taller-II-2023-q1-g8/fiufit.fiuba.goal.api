from abc import abstractmethod, ABC
from datetime import datetime

from src.domain.metric.metric import Metric


class Goal(ABC):
    def __init__(self, goal_dict: dict, metric_factory):
        """Initializes the goal with a dict."""
        self.id = goal_dict["_id"]
        self._username = goal_dict["username"]
        self._starting_date = goal_dict["starting_date"]
        self._deadline = goal_dict["deadline"]
        self._metrics = [
            metric_factory.from_dict(metric_dict)
            for metric_dict in goal_dict["metrics"]
        ]

    @abstractmethod
    def current_value(self) -> float:
        """The current value of the goal."""
        raise NotImplementedError

    @abstractmethod
    def goal_value(self) -> float:
        """The goal value to be completed."""
        raise NotImplementedError

    def metrics(self) -> list[Metric]:
        """The metrics of the goal."""
        return self._metrics

    def starting_date(self) -> datetime:
        """The starting date of the goal."""
        return self._starting_date

    def deadline(self) -> datetime:
        """The deadline of the goal."""
        return self._deadline

    def was_completed(self) -> bool:
        """Returns True if the goal has been completed."""
        return self.current_value() >= self.goal_value()

    def in_progress(self) -> bool:
        """Returns True if the goal is in progress."""
        return not self.was_completed() and not self.was_failed()

    def completion_percentage(self) -> float:
        """The percentage of the goal completion."""
        completion_fraction = min(1.0, self.current_value() / self.goal_value())

        return 100 * completion_fraction

    def was_failed(self) -> bool:
        """Returns True if the deadline has passed."""
        return self.deadline() < datetime.now() and not self.was_completed()
