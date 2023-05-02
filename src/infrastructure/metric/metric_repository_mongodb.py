"""MongoDB repository for metrics""" ""
from bson import ObjectId

from src.domain.repository import IRepository


class MetricRepositoryMongoDB(IRepository):
    """MongoDB repository for metrics"""

    def __init__(self, metric_collection):
        self._collection = metric_collection

    def load_by_id(self, id: str) -> dict:
        """Load a metric by id"""
        query = {"_id": ObjectId(id)}
        result = self._collection.find_one(query)
        if result is not None:
            result["_id"] = str(result["_id"])
        return result

    def load_all(self) -> list[dict]:
        """Load all metrics"""
        metrics = [metric for metric in self._collection.find({})]
        for i in range(len(metrics)):
            metrics[i]["_id"] = str(metrics[i]["_id"])
        return metrics

    def create(self, metric_dict: dict) -> str:
        """Create a metric"""
        result = self._collection.insert_one(metric_dict)
        return str(result.inserted_id)

    def delete(self, metric_id: str) -> None:
        """Delete a metric"""
        self._collection.delete_one({"_id": ObjectId(metric_id)})
