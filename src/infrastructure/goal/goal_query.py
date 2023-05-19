"""Used for performing complex queries on the goal collection."""


class GoalQuery:
    def __init__(self, collection, goal_factory, metric_query):
        self._collection = collection
        self._metric_query = metric_query
        self._goal_factory = goal_factory

    def load_matching(
        self, username: str | None = None, goal_type: str | None = None, status: str = ""
    ) -> list[dict]:
        """Load goals with optional filters"""

        query = {"$and": []}

        if username is not None:
            query["$and"].append({"username": username})
        if goal_type is not None:
            query["$and"].append({"type": goal_type})
        if query["$and"] == []:
            query = {}

        goal_dicts = [goal_dict for goal_dict in self._collection.find(query)]

        for i in range(len(goal_dicts)):
            goal_dicts[i]["_id"] = str(goal_dicts[i]["_id"])
            goal_dicts[i]["metrics"] = self._metric_query.load_related_metrics(
                goal_dicts[i]
            )

        return self._filter_goals_by_status(goal_dicts, status)

    def _filter_goals_by_status(
        self, goals: list[dict], status: str | None
    ) -> list[dict]:
        """Filter goals by status"""

        match status:
            case "in_progress":
                return list(
                    filter(
                        lambda goal: self._goal_factory.from_dict(goal).in_progress(),
                        goals,
                    )
                )
            case "failed":
                return list(
                    filter(
                        lambda goal: self._goal_factory.from_dict(goal).was_failed(),
                        goals,
                    )
                )
            case "completed":
                return list(
                    filter(
                        lambda goal: self._goal_factory.from_dict(goal).was_completed(),
                        goals,
                    )
                )
            case _:
                return goals
