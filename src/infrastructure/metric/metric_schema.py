"""Used to validate the data that is sent to the metric service"""
from datetime import datetime
from typing import Union
from pydantic import BaseModel, validator


class TrainingPlanCompletedSchema(BaseModel):
    type: str
    username: str
    created_at: datetime
    plan_title: str

    @validator("created_at", pre=True)
    def validate_created_at(cls, v):
        return datetime.fromisoformat(v.replace("Z", "+00:00"))

    @validator("type")
    def type_must_be_training_plan_completion(cls, type):
        if type != "training_plan_completed":
            raise ValueError("type must be training_plan_completed")
        return type


class ExerciseSetCompletedSchema(BaseModel):
    type: str
    username: str
    created_at: datetime
    exercise_title: str
    reps: int
    weight_in_kg: float

    @validator("created_at", pre=True)
    def validate_created_at(cls, v):
        return datetime.fromisoformat(v.replace("Z", "+00:00"))

    @validator("type")
    def type_must_be_exercise_set_completed(cls, type):
        if type != "exercise_set_completed":
            raise ValueError("type must be exercise_set_completed")
        return type


MetricSchema = Union[ExerciseSetCompletedSchema, TrainingPlanCompletedSchema]
