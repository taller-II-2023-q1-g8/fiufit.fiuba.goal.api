import pytest
from pydantic import ValidationError
from src.infrastructure.goal.goal_schema import TotalStepsTakenSchema


def test_can_create_total_steps_taken_schema():
    TotalStepsTakenSchema(
        type="total_steps_taken",
        username="Martin",
        goal_num_of_steps=100,
        starting_date="2021-01-01T00:00:00Z",
        deadline="2052-01-08T00:00:00Z",
    )


def test_fails_if_missing_goal_num_of_steps():
    with pytest.raises(ValidationError):
        TotalStepsTakenSchema(
            type="total_steps_taken",
            username="Martin",
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )


def test_fails_if_goal_num_of_steps_is_negative():
    with pytest.raises(ValidationError):
        TotalStepsTakenSchema(
            type="total_steps_taken",
            username="Martin",
            goal_num_of_steps=-100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )


def test_steps_fails_if_no_username():
    with pytest.raises(ValidationError):
        TotalStepsTakenSchema(
            type="total_steps_taken",
            goal_num_of_steps=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )

def test_steps_fails_if_username_is_empty():
    with pytest.raises(ValidationError):
        TotalStepsTakenSchema(
            type="total_steps_taken",
            username="",
            goal_num_of_steps=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )


def test_steps_fails_if_deadline_is_before_start():
    with pytest.raises(ValidationError):
        TotalStepsTakenSchema(
            type="total_steps_taken",
            username="Martin",
            goal_num_of_steps=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2000-01-08T00:00:00Z",
        )


def test_steps_fails_if_deadline_is_wrong():
    with pytest.raises(ValidationError):
        TotalStepsTakenSchema(
            type="total_steps_taken",
            username="Martin",
            goal_num_of_steps=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="e",
        )


def test_steps_fails_if_starting_date_is_wrong():
    with pytest.raises(ValidationError):
        TotalStepsTakenSchema(
            type="total_steps_taken",
            username="Martin",
            goal_num_of_steps=100,
            starting_date="a",
            deadline="2052-01-08T00:00:00Z",
        )


def test_fails_if_type_is_not_total_steps_taken():
    with pytest.raises(ValidationError):
        TotalStepsTakenSchema(
            type="steps",
            username="Martin",
            goal_num_of_steps=100,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )
