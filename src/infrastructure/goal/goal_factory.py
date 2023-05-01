"""Used for mapping dictionaries to Goal domain objects."""""
from src.domain.goal.goal import Goal
from src.domain.goal.max_weight_lifted_in_exercise import\
    MaxWeightLiftedInExercise
from src.domain.goal.training_plan_completion import TrainingPlanCompletion


class GoalFactory:
    def __init__(self, metric_factory):
        self._metric_factory = metric_factory

    def from_dict(self, goal_dict: dict) -> Goal:
        """Creates a goal from a dictionary."""

        match goal_dict['type']:
            case 'training_plan_completion':
                return TrainingPlanCompletion(
                        goal_dict,
                        self._metric_factory)
            case 'max_weight_lifted_in_exercise':
                return MaxWeightLiftedInExercise(
                        goal_dict,
                        self._metric_factory)
            case _:
                raise ValueError(
                    f"Unknown goal type: {goal_dict['type']}")