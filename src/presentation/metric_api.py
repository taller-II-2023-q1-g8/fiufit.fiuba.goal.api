"""Metric API Router"""
from datetime import datetime
from fastapi import APIRouter
from src.infrastructure.metric.metric_schema import MetricSchema

# Dependencies
from src.config import metrics_service

metrics_routes = APIRouter(prefix="/metrics")


@metrics_routes.get("/", status_code=200, response_description="metrics")
async def requests_metrics_matching(
    username: str | None = None,
    type: str | None = None,
    from_date: str | None = None,
    to_date: str | None = None,
):
    """User Requests Metrics"""

    # Turn date strings into datetime objects
    from_date = datetime.fromisoformat(from_date) if from_date else None
    to_date = datetime.fromisoformat(to_date) if to_date else None

    # Perform query
    results = metrics_service.user_requests_metrics_matching(
        username, type, from_date, to_date
    )

    metrics = []

    # Convert metric ids to strings
    for metric in results:
        metric["_id"] = str(metric["_id"])
        metrics.append(metric)

    return metrics


@metrics_routes.get("/{metric_id}", status_code=200, response_description="metric")
async def wants_metric_with_id(metric_id: str):
    """User Requests Metric With Id"""
    metric = metrics_service.user_wants_metric_with_id(metric_id)

    # Conver metric id to string
    if metric is not None:
        metric["_id"] = str(metric["_id"])
    return metric


@metrics_routes.post("/", status_code=200, response_description="metric")
async def save_metric(metric: MetricSchema):
    """User Saves Metric"""
    return metrics_service.user_wants_to_create_metric(metric.dict())


@metrics_routes.delete("/{metric_id}", status_code=200, response_description="metric")
async def delete_metric_with_id(metric_id: str):
    """User Deletes Metric With Id"""
    return metrics_service.user_wants_to_delete_metric_with_id(metric_id)