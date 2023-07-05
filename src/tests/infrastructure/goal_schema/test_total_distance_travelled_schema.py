import pytest
from pydantic import ValidationError
from src.infrastructure.goal.goal_schema import TotalDistanceTravelledSchema


def test_can_create_total_distance_travelled_schema():
    TotalDistanceTravelledSchema(
        type="total_distance_travelled",
        username="Martin",
        goal_distance_in_meters=10000,
        starting_date="2021-01-01T00:00:00Z",
        deadline="2052-01-08T00:00:00Z",
    )


def test_fails_is_username_is_empty():
    with pytest.raises(ValidationError):
        TotalDistanceTravelledSchema(
            type="total_distance_travelled",
            username="",
            goal_distance_in_meters=10000,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )


def test_fails_is_missing_username():
    with pytest.raises(ValidationError):
        TotalDistanceTravelledSchema(
            type="total_distance_travelled",
            goal_distance_in_meters=10000,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )


def test_fails_is_missing_goal_distance():
    with pytest.raises(ValidationError):
        TotalDistanceTravelledSchema(
            type="total_distance_travelled",
            goal_distance_in_meters=10000,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )


def test_fails_if_goal_distance_is_negative():
    with pytest.raises(ValidationError):
        TotalDistanceTravelledSchema(
            type="total_distance_travelled",
            username="Martin",
            goal_distance_in_meters=-10000,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )

    with pytest.raises(ValidationError):
        TotalDistanceTravelledSchema(
            type="total_distance_travelled",
            username="Martin",
            goal_distance_in_meters=10000,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2w33:00:00Z",
        )


def test_distance_fails_if_starting_date_is_wrong():
    with pytest.raises(ValidationError):
        TotalDistanceTravelledSchema(
            type="total_distance_travelled",
            username="Martin",
            goal_distance_in_meters=10000,
            starting_date="aa3344",
            deadline="2052-01-08T00:00:00Z",
        )


def test_steps_fails_if_deadline_is_before_start():
    with pytest.raises(ValidationError):
        TotalDistanceTravelledSchema(
            type="total_distance_travelled",
            username="Martin",
            goal_distance_in_meters=10000,
            starting_date="2053-01-08T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )


def test_fails_if_type_is_not_total_distance_travelled():
    with pytest.raises(ValidationError):
        TotalDistanceTravelledSchema(
            type="distance_travelled",
            username="Martin",
            goal_distance_in_meters=10000,
            starting_date="2021-01-01T00:00:00Z",
            deadline="2052-01-08T00:00:00Z",
        )
