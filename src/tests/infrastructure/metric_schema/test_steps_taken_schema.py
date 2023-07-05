import pytest
from pydantic import ValidationError
from src.infrastructure.metric.metric_schema import StepsTakenSchema

def test_can_create_steps_taken_schema():
    StepsTakenSchema(
        type="steps_taken",
        username="Martin",
        step_count=10000,
        duration_in_seconds=3600,
        created_at="2021-01-01T00:00:00Z",
    )

def test_fails_if_date_is_wrong():
    with pytest.raises(ValidationError):
        StepsTakenSchema(
            type="steps_taken",
            username="Martin",
            step_count=10000,
            duration_in_seconds=3600,
            created_at="22w-01-01T00:00:00Z",
        )

def test_fails_if_type_is_wrong():
    with pytest.raises(ValidationError):
        StepsTakenSchema(
            type="steps",
            username="Martin",
            step_count=10000,
            duration_in_seconds=3600,
            created_at="2021-01-01T00:00:00Z",
        )

def test_fails_if_step_count_is_negative():
    with pytest.raises(ValidationError):
        StepsTakenSchema(
            type="steps_taken",
            username="Martin",
            step_count=-10000,
            duration_in_seconds=3600,
            created_at="2021-01-01T00:00:00Z",
        )

def test_fails_if_duration_is_negative():
    with pytest.raises(ValidationError):
        StepsTakenSchema(
            type="steps_taken",
            username="Martin",
            step_count=10000,
            duration_in_seconds=-10,
            created_at="2021-01-01T00:00:00Z",
        )
    
    