"""Goal repository implementation for MongoDB"""
from src.domain.repository import IRepository
from bson import ObjectId


class GoalRepositoryMongoDB(IRepository):
    """MongoDB repository for goals"""

    def __init__(
        self,
        goal_collection,
        metrics_query_module,
        metric_factory,
    ):
        self._collection = goal_collection
        self._metrics_query = metrics_query_module
        self._metric_factory = metric_factory

    def load_by_id(self, goal_id: str) -> dict:
        """Load goal by id"""
        goal = self._collection.find_one({"_id": ObjectId(goal_id)})
        goal["metrics"] = self._metrics_query.load_related_metrics(goal)
        goal["_id"] = str(goal["_id"])
        return goal

    def load_all(self) -> list[dict]:
        """Load all goals"""
        goals = [goal for goal in self._collection.find({})]
        for i in range(len(goals)):
            goals[i]["metrics"] = self._metrics_query.load_related_metrics(goals[i])
            goals[i]["_id"] = str(goals[i]["_id"])
        return goals

    def create(self, goal_dict: dict) -> str:
        """Create a goal"""
        result = self._collection.insert_one(goal_dict)
        return str(result.inserted_id)

    def delete(self, goal_id: str) -> None:
        """Delete a goal"""
        self._collection.delete_one({"_id": ObjectId(goal_id)})
