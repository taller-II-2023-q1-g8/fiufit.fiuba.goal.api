from bson import ObjectId

class NotificationRepositoryMongoDB():
    def __init__(self, notification_collection):
        self._collection = notification_collection

    def new_goal_completed(self, username: str, goal_id: str):
        new_notification = {
            "username": username,
            "type": "goal_completed",
            "goal_id": goal_id,
            "acknowledged": False,
        }
        
        self._collection.insert_one(new_notification)

    def get_not_acknowledged_by_username(self, username: str) -> list[dict]:
        """Get notifications by username"""
        notifications =  [n for n in self._collection.find({"username": username, "acknowledged": False})]

        for i in range(len(notifications)):
            notifications[i]["_id"] = str(notifications[i]["_id"])

        return notifications
    
    def acknowledge_by_id(self, notification_id: str):
        """Acknowledge notification by id"""
        self._collection.update_one({"_id": ObjectId(notification_id)}, {"$set": {"acknowledged": True}})