"""Used for mapping dictionaries to Metric domain objects.""" ""
from src.domain.metric.metric import (
    # CaloriesBurned,
    # DistanceTravelled,
    ExerciseSetCompleted,
    Metric,
    StepsTaken,
    TrainingPlanCompleted,
    # WeightMeasured,
)


class MetricFactory:
    def from_dict(self, metric_dict: dict) -> Metric:
        """Build a metric from a dictionary"""
        match metric_dict["type"]:
            case "training_plan_completed":
                return TrainingPlanCompleted(metric_dict)
            case "exercise_set_completed":
                return ExerciseSetCompleted(metric_dict)
            case "steps_taken":
                return StepsTaken(metric_dict)
            # case "weight_measured":
            #     return WeightMeasured(metric_dict)
            # case "distance_travelled":
            #     return DistanceTravelled(metric_dict)
            # case "calories_burned":
            #     return CaloriesBurned(metric_dict)
            case _:
                raise ValueError(f"Invalid metric type {metric_dict['type']}")
