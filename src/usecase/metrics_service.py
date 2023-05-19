"""Metric use case module."""
from datetime import datetime

from src.domain.repository import IRepository


class MetricService:
    def __init__(self, metric_repository: IRepository, metrics_query, goals_query, goal_completion_notifier):
        self._repository = metric_repository
        self._goals_query = goals_query
        self._metrics_query = metrics_query
        self._goal_completion_notifier = goal_completion_notifier

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

    def user_wants_to_create_metric(self, metric_dict: dict) -> str:
        """User wants to save a metric"""
        user_completed_goals = self._goals_query.load_matching(
            username=metric_dict["username"],
            status="completed"
        )
        user_completed_goals_ids = list(map(lambda goal: goal["_id"], user_completed_goals))

        new_metric_id = self._repository.create(metric_dict)

        user_completed_goals_refreshed = self._goals_query.load_matching(
            username=metric_dict["username"],
            status="completed",
        )

        user_completed_goals_ids_refreshed = list(map(lambda goal: goal["_id"], user_completed_goals_refreshed))

        for goal_id in user_completed_goals_ids_refreshed:
            if goal_id not in user_completed_goals_ids:
                self._goal_completion_notifier.new_goal_completed(metric_dict["username"], goal_id)
        
        return new_metric_id

    def user_wants_to_delete_metric_with_id(self, metric_id: str):
        """User wants to delete a goal"""
        return self._repository.delete(metric_id)