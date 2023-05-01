"""Used to validate the data that is sent to the metric service"""
from typing import Union
from pydantic import BaseModel, validator


class TrainingPlanCompletedSchema(BaseModel):
    type: str
    username: str
    created_at: str
    plan_title: str

    @validator('type')
    def type_must_be_training_plan_completion(cls, type):
        if type != "training_plan_completed":
            raise ValueError("type must be training_plan_completed")
        return type


class ExcerciseSetCompletedSchema(BaseModel):
    type: str
    username: str
    created_at: str
    exercise_title: str
    reps: int
    weight_in_kg: float

    @validator('type')
    def type_must_be_exercise_set_completed(cls, type):
        if type != "exercise_set_completed":
            raise ValueError("type must be exercise_set_completed")
        return type


class MetricSchema(BaseModel):
    metric: Union[ExcerciseSetCompletedSchema, TrainingPlanCompletedSchema]