import pytest
from pydantic import ValidationError
from src.infrastructure.metric.metric_schema import TrainingPlanCompletedSchema

def test_can_create_training_plan_completed_schema():
    TrainingPlanCompletedSchema(
        type="training_plan_completed",
        username="Martin",
        plan_title="Road to Olympus",
        created_at="2021-01-01T00:00:00Z",
    )


def test_fails_if_starting_date_is_wrong():
    with pytest.raises(ValidationError):
        TrainingPlanCompletedSchema(
            type="training_plan_completed",
            username="Martin",
            plan_title="Road to Olympus",
            created_at="22w-01-01T00:00:00Z",
        )

def test_fails_if_type_is_wrong():
    with pytest.raises(ValidationError):
        TrainingPlanCompletedSchema(
            type="training_plan",
            username="Martin",
            plan_title="Road to Olympus",
            created_at="2021-01-01T00:00:00Z",
        )