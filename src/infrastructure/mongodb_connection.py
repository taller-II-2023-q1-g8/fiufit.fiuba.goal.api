"""Database Connection"""
import os
import pymongo


if os.environ.get("DB_URL") is not None:
    print("Using DB_URL found in environment.")
    client = pymongo.MongoClient(os.environ.get("DB_URL"))
else:
    print("No DB_URL environment variable found. Using default.")
    client = pymongo.MongoClient("mongodb://mongodb:27017")
    print("Connected")

metrics_and_goals_db = client["goals_and_metrics"]
metrics_collection = metrics_and_goals_db["metrics"]
goals_collection = metrics_and_goals_db["goals"]
notifications_collection = metrics_and_goals_db["notifications"]
