from fastapi import FastAPI
from src.presentation.goal_api import goals_routes

"""
Application Entry Point
"""

app = FastAPI()
app.include_router(goals_routes)

@app.get("/healthcheck")
async def root():
    """Healthcheck endpoint"""
    return "Goals Microservice is up and running"
