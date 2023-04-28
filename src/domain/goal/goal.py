from abc import abstractmethod
from datetime import datetime

from src.domain.metric.metric import Metric


class Goal:
    @abstractmethod
    def was_achieved(self) -> bool:
        """Returns True if the goal has been achieved."""
        raise NotImplementedError

    @abstractmethod
    def completion_percentage(self) -> float:
        """The percentage of the goal completion."""
        raise NotImplementedError

    @abstractmethod
    def was_failed(self) -> bool:
        """Returns True if the deadline has passed."""
        raise NotImplementedError

    @abstractmethod
    def deadline(self) -> datetime:
        """The deadline of the goal."""
        raise NotImplementedError

    @abstractmethod
    def goal_value(self) -> float:
        """The goal value to be achieved."""
        raise NotImplementedError

    @abstractmethod
    def unit(self) -> str:
        """The unit of the goal value."""
        raise NotImplementedError

    @abstractmethod
    def metrics(self) -> list[Metric]:
        """The metrics that are used to measure the goal progress."""
        raise NotImplementedError
