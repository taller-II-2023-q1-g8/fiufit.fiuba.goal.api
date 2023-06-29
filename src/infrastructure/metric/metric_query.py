"""Used for performing complex queries on the metrics collection"""


class MetricsQuery:
    def __init__(self, collection):
        self._collection = collection

    def load_related_metrics(self, goal_dict: dict) -> list[dict]:
        """Load metrics related to a goal"""

        query = {
            "username": goal_dict["username"],
            "from_date": goal_dict["starting_date"],
            "to_date": goal_dict["deadline"],
        }

        print(f"DEBUG: Loading Related Metrics for: {goal_dict['_id']}")
        match goal_dict["type"]:
            case "training_plan_completion":
                query["type"] = "training_plan_completed"
            case "max_weight_lifted_in_exercise":
                query["type"] = "exercise_set_completed"
                query["exercise_title"] = goal_dict["exercise_title"]
            case "total_steps_taken":
                query["type"] = "steps_taken"
            case _:
                raise ValueError(f"Unknown goal type: {goal_dict['type']}")

        return self.load_matching(query)

    def load_matching(self, query_params: dict) -> list[dict]:
        # TODO Make values a dictionary
        """Turns query parameters into a MongoDB query and returns metrics"""

        db_query = {"$and": []}

        # Date queries
        if "from_date" in query_params:
            db_query["$and"].append(
                {"created_at": {"$gte": query_params.pop("from_date")}}
            )

        if "to_date" in query_params:
            db_query["$and"].append(
                {"created_at": {"$lte": query_params.pop("to_date")}}
            )

        # Other queries
        for query_param, value in query_params.items():
            db_query["$and"].append({query_param: value})

        # If no query, return all metrics
        if db_query["$and"] == []:
            db_query = {}

        metrics = [metric for metric in self._collection.find(db_query)]
        for i in range(len(metrics)):
            metrics[i]["_id"] = str(metrics[i]["_id"])

        return metrics
