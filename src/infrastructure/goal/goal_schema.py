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

    @validator('goal_weight_in_kg')
    def goal_num_of_completions_must_be_positive(cls, v):
        if v < 1:
            raise ValueError('Goal weight must be positive')
        return v

    @validator('deadline')
    def deadline_must_be_after_starting_date(cls, v, values):
        starting_date = datetime.fromisoformat(values['starting_date'])
        deadline = datetime.fromisoformat(v)
        if starting_date >= deadline:
            raise ValueError('Goal deadline must be after starting date')
        return v


class TrainingPlanCompletionSchema(BaseModel):
    type: str
    username: str
    goal_num_of_completions: int
    starting_date: str
    deadline: str

    @validator('goal_num_of_completions')
    def goal_num_of_completions_must_be_positive(cls, v):
        if v < 1:
            raise ValueError('Goal number of completions must be positive')
        return v

    @validator('deadline')
    def deadline_must_be_after_starting_date(cls, v, values):
        starting_date = datetime.fromisoformat(values['starting_date'])
        deadline = datetime.fromisoformat(v)
        if starting_date >= deadline:
            raise ValueError('Goal deadline must be after starting date')
        return v


class GoalSchema(BaseModel):
    goal: Union[
        TrainingPlanCompletionSchema,
        MaxWeightLiftedInExcerciseSchema
    ]
