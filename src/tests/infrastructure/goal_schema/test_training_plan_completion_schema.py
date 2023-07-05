import pytest
from pydantic import ValidationError
from src.infrastructure.goal.goal_schema import TrainingPlanCompletionSchema

# Total distance travelled

import pytest
from pydantic import ValidationError
from src.infrastructure.goal.goal_schema import TrainingPlanCompletionSchema


def test_can_create_training_plan_completion_schema():
    TrainingPlanCompletionSchema(
        type="training_plan_completion",
        username="Martin",
        goal_num_of_completions=100,
        starting_date="2021-01-01T00:00:00Z",
        deadline="2052-01-08T00:00:00Z",
    )

def test_fails_if_empty_username():
    with pytest.raises(ValidationError):
        TrainingPlanCompletionSchema(
            type="training_plan_completion",
            username="",
            goal_num_of_completions=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )

def test_fails_if_type_is_wrong():
    with pytest.raises(ValidationError):
        TrainingPlanCompletionSchema(
            type="training_plan",
            username="Franco",
            goal_num_of_completions=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )

def test_fails_if_starting_date_is_wrong():
    with pytest.raises(ValidationError):
        TrainingPlanCompletionSchema(
            type="training_plan_completion",
            username="Franco",
            goal_num_of_completions=100,
            starting_date="22w-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )

def test_fails_if_deadline_is_wrong():
    with pytest.raises(ValidationError):
        TrainingPlanCompletionSchema(
            type="training_plan_completion",
            username="Franco",
            goal_num_of_completions=100,
            deadline="22w-01-01T00:00:00Z",
            starting_date="2052-01-08T00:00:00Z",
        )

def test_fails_if_deadline_is_before_starting_date():
    with pytest.raises(ValidationError):
        TrainingPlanCompletionSchema(
            type="training_plan_completion",
            username="Franco",
            goal_num_of_completions=100,
            deadline="2023-01-08T00:00:00Z",
            starting_date="2052-01-08T00:00:00Z",
        )

def test_fails_if_goal_is_negative():
    with pytest.raises(ValidationError):
        TrainingPlanCompletionSchema(
            type="training_plan_completion",
            username="Martin",
            goal_num_of_completions=-100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )