"""User API Router"""
from fastapi import APIRouter


goals_routes = APIRouter(prefix="/goals")
# goals_repository = UserTable()
# goals_service = UserService(goals_repository)  # Application Service

@goals_routes.get("/", status_code=200, response_description="index")
async def index(username: str):
    """Root Directory"""
    return "Goals Microservice"
