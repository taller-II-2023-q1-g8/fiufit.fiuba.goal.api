"""Used to validate the data that is sent to the goal service."""
from datetime import datetime
from typing import Union
from pydantic import BaseModel, validator


class MaxWeightLiftedInExerciseSchema(BaseModel):
    type: str
    username: str
    exercise_title: str
    goal_weight_in_kg: float
    starting_date: str
    deadline: str

    @validator("type")
    def type_must_be_valid(cls, v):
        if v != "max_weight_lifted_in_exercise":
            raise ValueError("Type must be max_weight_lifted_in_exercise")

    @validator("starting_date")
    def parse_starting_date(cls, starting_date):
        return datetime.fromisoformat(starting_date.replace("Z", "+00:00"))

    @validator("deadline")
    def parse_deadline(cls, deadline, values):
        deadline = datetime.fromisoformat(deadline.replace("Z", "+00:00"))
        if deadline < values["starting_date"]:
            raise ValueError("Goal deadline must be after starting date")
        return deadline

    @validator("goal_weight_in_kg")
    def goal_goal_weight_in_kg_must_be_positive(cls, v):
        if v < 1:
            raise ValueError("Goal weight must be positive")
        return v
    
    @validator("exercise_title")
    def exercise_title_must_be_valid(cls, v):
        if not v:
            raise ValueError("Exercise title must not be empty")
        return v

    @validator("username")
    def username_must_be_valid(cls, v):
        if not v:
            raise ValueError("Username must not be empty")
        return v


class TrainingPlanCompletionSchema(BaseModel):
    type: str
    starting_date: str
    deadline: str
    username: str
    goal_num_of_completions: int

    @validator("username")
    def username_must_be_valid(cls, v):
        if not v:
            raise ValueError("Username must not be empty")
        return v

    @validator("type")
    def type_must_be_valid(cls, v):
        if v != "training_plan_completion":
            raise ValueError("Type must be training_plan_completion")

    @validator("starting_date")
    def parse_starting_date(cls, starting_date):
        return datetime.fromisoformat(starting_date.replace("Z", "+00:00"))

    @validator("deadline")
    def parse_deadline(cls, deadline, values):
        deadline = datetime.fromisoformat(deadline.replace("Z", "+00:00"))
        if deadline < values["starting_date"]:
            raise ValueError("Goal deadline must be after starting date")
        return deadline

    @validator("goal_num_of_completions")
    def goal_num_of_completions_must_be_positive(cls, v):
        if v < 1:
            raise ValueError("Goal number of completions must be positive")
        return v


GoalSchema = Union[TrainingPlanCompletionSchema, MaxWeightLiftedInExerciseSchema]
