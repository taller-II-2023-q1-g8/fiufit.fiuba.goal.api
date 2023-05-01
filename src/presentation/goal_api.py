"""Goal API Router"""
from datetime import datetime
from fastapi import APIRouter, HTTPException
from src.infrastructure.goal.goal_schema import GoalSchema

from src.infrastructure.dependency_injection import goals_service

goals_routes = APIRouter(prefix="/goal")
goal_statuses = ["in_progress", "completed", "failed"]


@goals_routes.get("/", status_code=200, response_description="goals")
async def requests_goals_matching(
    username: str | None = None,
    type: str | None = None,
    status: str | None = None
):
    """User Requests Goals"""

    if status is not None and status not in goal_statuses:
        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )

    return goals_service.user_requests_goals(
        username,
        type,
        status
    )


@goals_routes.get("/{goal_id}", status_code=200, response_description="goal")
async def requests_goal_with_id(goal_id: str):
    """User Requests Goal With Id"""
    goal = goals_service.user_wants_goal_with_id(goal_id)

    # Display ObjectIds as strings
    if goal is not None:
        goal['_id'] = str(goal['_id'])
        for i in range(len(goal['metrics'])):
            goal['metrics'][i]['_id'] = str(goal['metrics'][i]['_id'])

    return goal


@goals_routes.delete("/{goal_id}", status_code=200,
                     response_description="goal")
async def wants_to_delete_goal_with_id(goal_id: str):
    return goals_service.user_wants_to_delete_goal_with_id(goal_id)


@goals_routes.put("/", status_code=200, response_description="goal")
async def wants_to_create_metric(goal: dict) -> str:
    """User Saves Metric"""

    # Validate data
    GoalSchema(**{'goal': goal})

    # Turn date strings into datetime objects
    goal['starting_date'] = datetime.fromisoformat(goal['starting_date'])
    goal['deadline'] = datetime.fromisoformat(goal['deadline'])

    # Create goal
    return goals_service.user_wants_to_create_goal(goal)
