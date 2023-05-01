from datetime import datetime
from src.domain.goal.goal import Goal
from src.domain.metric.metric import Metric, TrainingPlanCompleted


class TrainingPlanCompletion(Goal):
    """A goal that represents the repeated completion of a training plan."""
    def _check_required_keys(self, d: dict, required_keys: list[str]):
        """Checks that the required keys are present in the dict."""
        missing_keys = [key for key in required_keys if key not in d]
        if missing_keys:
            raise ValueError(
                f"Invalid goal dictionary, missing f{missing_keys}"
            )

    def to_dict(self) -> dict:
        """Returns a dict representation of the goal."""
        return {
            "id": self.id,
            "goal_num_of_completions": self._goal_num_of_completions,
            "starting_date": self._starting_date,
            "deadline": self._deadline,
            "metrics": self._metrics
        }

    def __init__(self, goal_dict: dict, metric_factory):
        """Initializes the goal with a dict."""

        self.id = goal_dict["_id"]
        self._goal_num_of_completions = goal_dict["goal_num_of_completions"]
        self._username = goal_dict["username"]
        self._starting_date = goal_dict["starting_date"]
        self._deadline = goal_dict["deadline"]
        self._metrics = [
            metric_factory.from_dict(metric_dict) for
            metric_dict in goal_dict["metrics"]
        ]

    def was_completed(self) -> bool:
        """Returns True if the goal has been completed."""
        return len(self._metrics) >= self._goal_num_of_completions

    def completion_percentage(self) -> float:
        """The percentage of the goal completion."""
        return 100 * min(1.0, len(self._metrics)/self._goal_num_of_completions)

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
        return self._goal_num_of_completions

    def add_metrics(self, metrics: list[Metric]):
        """Adds new metrics to the goal."""
        # TODO: Add validation that the metrics are not already in the goal

        metrics_to_add = list(filter(
            lambda metric:
                isinstance(metric, TrainingPlanCompleted) and
                metric.created_at > self._starting_date and
                metric.created_at < self._deadline,
                metrics
        ))

        self._metrics.extend(metrics_to_add)

    def metrics(self) -> list[Metric]:
        """The metrics that are used to measure the goal progress."""
        return self._metrics
