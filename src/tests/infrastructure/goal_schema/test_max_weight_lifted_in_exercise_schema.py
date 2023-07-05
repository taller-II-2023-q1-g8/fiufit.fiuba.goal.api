import pytest
from pydantic import ValidationError
from src.infrastructure.goal.goal_schema import MaxWeightLiftedInExerciseSchema

def test_can_create_max_weight_lifted_in_exercise_schema():
    MaxWeightLiftedInExerciseSchema(
        exercise_title="Bench press",
        type="max_weight_lifted_in_exercise",
        username="Martin",
        goal_weight_in_kg=100,
        starting_date="2021-01-01T00:00:00Z",
        deadline="2052-01-08T00:00:00Z",
    )


def test_fails_if_missing_exercise_title():
    with pytest.raises(ValidationError):
        MaxWeightLiftedInExerciseSchema(
            type="max_weight_lifted_in_exercise",
            username="Martin",
            goal_weight_in_kg=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )

def test_fails_if_exercise_title_is_empty():
    with pytest.raises(ValidationError):
        MaxWeightLiftedInExerciseSchema(
            type="max_weight_lifted_in_exercise",
            exercise_title="",
            username="Martin",
            goal_weight_in_kg=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )

def test_fails_if_username_is_empty():
    with pytest.raises(ValidationError):
        MaxWeightLiftedInExerciseSchema(
            type="max_weight_lifted_in_exercise",
            exercise_title="Bench Press",
            username="",
            goal_weight_in_kg=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )


def test_fails_if_missing_goal_weight():
    with pytest.raises(ValidationError):
        MaxWeightLiftedInExerciseSchema(
            type="max_weight_lifted_in_exercise",
            username="Martin",
            exercise_title="Bench press",
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )


def test_fails_if_goal_weight_is_negative():
    with pytest.raises(ValidationError):
        MaxWeightLiftedInExerciseSchema(
            type="max_weight_lifted_in_exercise",
            username="Martin",
            exercise_title="Bench press",
            goal_weight_in_kg=-100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )

def test_fails_if_deadline_is_before_start():
    with pytest.raises(ValidationError):
        MaxWeightLiftedInExerciseSchema(
            type="max_weight_lifted_in_exercise",
            username="Martin",
            exercise_title="Bench press",
            goal_weight_in_kg=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2001-01-08T00:00:00Z",
        )


def test_fails_if_type_is_not_max_weight_lifted_in_exercise():
    with pytest.raises(ValidationError):
        MaxWeightLiftedInExerciseSchema(
            type="max_weight",
            username="Martin",
            exercise_title="Bench press",
            goal_weight_in_kg=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )


def test_max_weight_fails_if_no_username():
    with pytest.raises(ValidationError):
        MaxWeightLiftedInExerciseSchema(
            type="max_weight_lifted_in_exercise",
            exercise_title="Bench press",
            goal_weight_in_kg=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )


def test_max_weight_fails_if_starting_date_is_wrong():
    with pytest.raises(ValidationError):
        MaxWeightLiftedInExerciseSchema(
            type="max_weight_lifted_in_exercise",
            username="Martin",
            exercise_title="Bench press",
            goal_weight_in_kg=100,
            starting_date="sss",
            deadline="2052-01-08T00:00:00Z",
        )


def test_max_weight_fails_if_deadline_is_wrong():
    with pytest.raises(ValidationError):
        MaxWeightLiftedInExerciseSchema(
            type="max_weight_lifted_in_exercise",
            username="Martin",
            exercise_title="Bench press",
            goal_weight_in_kg=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="sse",
        )
