from datetime import datetime
from src.domain.goal.goal import Goal
from src.domain.metric.metric import Metric


class TrainingPlanCompletion(Goal):
    """A goal that represents the repeated completion of a training plan."""
    _unit = "plan(es) de entrenamiento"

    def __init__(
            self,
            goal_num_of_completions: float,
            deadline: datetime,
            metrics: list[Metric]
            ):
        self._goal_num_of_completions = goal_num_of_completions
        self._deadline = deadline
        self._metrics = metrics

    def was_achieved(self) -> bool:
        """Returns True if the goal has been achieved."""
        return len(self._metrics) >= self._goal_num_of_completions

    def completion_percentage(self) -> float:
        """The percentage of the goal completion."""
        return min(1.0, len(self._metrics)/self._goal_num_of_completions)

    def was_failed(self) -> bool:
        """Returns True if the deadline has passed."""
        return self._deadline < datetime.now() and not self.was_achieved()

    def deadline(self) -> datetime:
        """The deadline of the goal."""
        return self._deadline

    def goal_value(self) -> float:
        """The goal value to be achieved."""
        return self._goal_num_of_completions

    def unit(self) -> str:
        """The unit of the goal value."""
        return self._unit

    def metrics(self) -> list[Metric]:
        """The metrics that are used to measure the goal progress."""
        return self._metrics
