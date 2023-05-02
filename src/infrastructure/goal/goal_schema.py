"""Used to validate the data that is sent to the goal service."""
from datetime import datetime
from typing import Union
from pydantic import BaseModel, validator


class MaxWeightLiftedInExcerciseSchema(BaseModel):
    type: str
    username: str
    exercise_title: str
    goal_weight_in_kg: float
    starting_date: str
    deadline: str

    @validator("starting_date")
    def parse_starting_date(cls, starting_date):
        return datetime.fromisoformat(starting_date)

    @validator("deadline")
    def parse_deadline(cls, deadline, values):
        deadline = datetime.fromisoformat(deadline)
        if deadline < values["starting_date"]:
            raise ValueError("Goal deadline must be after starting date")
        return deadline

    @validator("goal_weight_in_kg")
    def goal_goal_weight_in_kg_must_be_positive(cls, v):
        if v < 1:
            raise ValueError("Goal weight must be positive")
        return v


class TrainingPlanCompletionSchema(BaseModel):
    type: str
    starting_date: str
    deadline: str
    username: str
    goal_num_of_completions: int

    @validator("starting_date")
    def parse_starting_date(cls, starting_date):
        return datetime.fromisoformat(starting_date)

    @validator("deadline")
    def parse_deadline(cls, deadline, values):
        deadline = datetime.fromisoformat(deadline)
        if deadline < values["starting_date"]:
            raise ValueError("Goal deadline must be after starting date")
        return deadline

    @validator("goal_num_of_completions")
    def goal_num_of_completions_must_be_positive(cls, v):
        if v < 1:
            raise ValueError("Goal number of completions must be positive")
        return v


GoalSchema = Union[TrainingPlanCompletionSchema, MaxWeightLiftedInExcerciseSchema]
