import pytest
from pydantic import ValidationError
from src.infrastructure.metric.metric_schema import ExerciseSetCompletedSchema

def test_can_create_exercise_set_completed_schema():
    ExerciseSetCompletedSchema(
        type="exercise_set_completed",
        username="Martin",
        exercise_title="Bench Press",
        reps=10,
        weight_in_kg=100,
        created_at="2021-01-01T00:00:00Z",
    )

def test_fails_if_date_is_wrong():
    with pytest.raises(ValidationError):
        ExerciseSetCompletedSchema(
            type="exercise_set_completed",
            username="Martin",
            exercise_title="Bench Press",
            reps=10,
            weight_in_kg=100,
            created_at="22w-01-01T00:00:00Z",
        )

def test_fails_if_type_is_wrong():
    with pytest.raises(ValidationError):
        ExerciseSetCompletedSchema(
            type="exercise_set",
            username="Martin",
            exercise_title="Bench Press",
            reps=10,
            weight_in_kg=100,
            created_at="2021-01-01T00:00:00Z",
        )