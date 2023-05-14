"""Metric use case module."""
from datetime import datetime

from src.domain.repository import IRepository


class MetricService:
    def __init__(self, metric_repository: IRepository, metrics_query):
        self._repository = metric_repository
        self._metrics_query = metrics_query

    def user_wants_metric_with_id(self, metric_id: str) -> dict:
        """User wants metric with id"""
        return self._repository.load_by_id(metric_id)

    def user_requests_metrics_matching(
        self,
        username: str | None,
        type: str | None,
        from_date: datetime | None,
        to_date: datetime | None,
    ) -> list[dict]:
        """User requests metrics with optional filters"""

        query_params = {}
        if username is not None:
            query_params["username"] = username
        if type is not None:
            query_params["type"] = type
        if from_date is not None:
            query_params["from_date"] = from_date
        if to_date is not None:
            query_params["to_date"] = to_date

        return self._metrics_query.load_matching(query_params)

    def user_wants_to_create_metric(self, metric_dict: dict) -> dict:
        """User wants to save a metric"""
        return self._repository.create(metric_dict)

    def user_wants_to_delete_metric_with_id(self, metric_id: str):
        """User wants to delete a goal"""
        return self._repository.delete(metric_id)