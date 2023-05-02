from src.domain.repository import IRepository


class GoalService(IRepository):
    def __init__(self, goal_repository, goal_query, goal_factory):
        self._repository = goal_repository
        self._goal_query = goal_query
        self._goal_factory = goal_factory

    def user_wants_goal_with_id(self, goal_id: str) -> dict:
        """User wants goal with id"""
        goal = self._repository.load_by_id(goal_id)
        if goal is not None:
            goal[
                "completion_percentage"
            ] = self.user_requests_goal_completion_percentage(goal)
            goal["status"] = self.user_requests_goal_status(goal)
        return goal

    def user_requests_goals(
        self, username: str | None, type: str | None, status: str | None
    ) -> list[dict]:
        """User requests goals with optional filters"""
        goals = self._goal_query.load_matching(username, type, status)
        for goal in goals:
            goal[
                "completion_percentage"
            ] = self.user_requests_goal_completion_percentage(goal)
            goal["status"] = self.user_requests_goal_status(goal)
        return goals

    def user_wants_to_create_goal(self, goal: dict) -> str:
        """User wants to save a goal"""
        return self._repository.create(goal)

    def user_requests_goal_status(self, goal_dict: dict) -> str:
        """User requests the status of a goal"""
        goal = self._goal_factory.from_dict(goal_dict)
        if goal.was_completed():
            return "completed"
        if goal.was_failed():
            return "failed"
        else:
            return "in_progress"

    def user_requests_goal_completion_percentage(self, goal_dict: dict) -> float:
        """User requests the status of a goal"""
        goal = self._goal_factory.from_dict(goal_dict)
        return goal.completion_percentage()

    def user_wants_to_delete_goal_with_id(self, goal_id: str):
        """User wants to delete a goal"""
        return self._repository.delete(goal_id)
