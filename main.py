from fastapi import FastAPI
from src.presentation.goal_api import goals_routes
from src.presentation.metric_api import metrics_routes

"""
Application Entry Point
"""

app = FastAPI()
app.include_router(goals_routes)
app.include_router(metrics_routes)


@app.get("/healthcheck")
async def root():
    """Healthcheck endpoint"""
    return "Goals and Metrics Microservice is up and running"
