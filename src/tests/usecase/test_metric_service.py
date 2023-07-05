import pytest
from src.usecase.metrics_service import MetricService


class MockRepo:
    def load_by_id(self, metric_id):
        return "Hello"

class MockQuery:
    def load_matching(self, query_params):
        return query_params

def test_user_wants_metric_with_id():
    goals_service = MetricService(
        metric_repository=MockRepo(),
        metrics_query=None,
        goals_query=None,
        goal_completion_notifier=None,
    )

    result = goals_service.user_wants_metric_with_id("as455443f")
    assert result == "Hello"


def test_user_requests_metrics_matching():
    goals_service = MetricService(
        metric_repository=MockRepo(),
        metrics_query=MockQuery(),
        goals_query=None,
        goal_completion_notifier=None,
    )

    expected_query = {
        "username": "Martin", 
        "type": "training_plan_completion", 
        "from_date": "2021-01-01T00:00:00Z",
        "to_date": "2021-02-01T00:00:00Z",}

    query_sent = goals_service.user_requests_metrics_matching(
        username="Martin",
        type="training_plan_completion",
        from_date="2021-01-01T00:00:00Z",
        to_date="2021-02-01T00:00:00Z",
    )

    assert query_sent == expected_query