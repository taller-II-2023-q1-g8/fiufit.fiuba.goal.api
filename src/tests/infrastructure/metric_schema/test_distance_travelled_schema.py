import pytest
from pydantic import ValidationError
from src.infrastructure.metric.metric_schema import DistanceTravelledSchema

def test_can_create_distance_travelled_schema():
    DistanceTravelledSchema(
        type="distance_travelled",
        username="Martin",
        distance_in_meters=10000,
        duration_in_seconds=3600,
        created_at="2021-01-01T00:00:00Z",
    )

def test_fails_if_date_is_wrong():
    with pytest.raises(ValidationError):
        DistanceTravelledSchema(
            type="distance_travelled",
            username="Martin",
            distance_in_meters=10000,
            duration_in_seconds=3600,
            created_at="22w-01-01T00:00:00Z",
        )

def test_fails_if_distance_is_not_positive():
    with pytest.raises(ValidationError):
        DistanceTravelledSchema(
            type="distance_travelled",
            username="Martin",
            distance_in_meters=-10000,
            duration_in_seconds=3600,
            created_at="2021-01-01T00:00:00Z",
        )

def test_fails_if_type_is_wrong():
    with pytest.raises(ValidationError):
        DistanceTravelledSchema(
            type="distance",
            username="Martin",
            distance_in_meters=10000,
            duration_in_seconds=3600,
            created_at="2021-01-01T00:00:00Z",
        )

def test_fails_if_duration_is_not_positive():
    with pytest.raises(ValidationError):
        DistanceTravelledSchema(
            type="distance_travelled",
            username="Martin",
            distance_in_meters=10000,
            duration_in_seconds=-10,
            created_at="2021-01-01T00:00:00Z",
        )