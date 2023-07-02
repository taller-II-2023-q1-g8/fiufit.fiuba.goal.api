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


class StepsTakenSchema(BaseModel):
    type: str
    username: str
    created_at: datetime
    step_count: int
    duration_in_seconds: int

    @validator("created_at", pre=True)
    def validate_created_at(cls, v):
        return datetime.fromisoformat(v.replace("Z", "+00:00"))

    @validator("type")
    def type_must_be_steps_taken(cls, type):
        if type != "steps_taken":
            raise ValueError("type must be steps_taken")
        return type

    @validator("step_count")
    def step_count_must_be_positive(cls, count):
        if int(count) <= 0:
            raise ValueError("step count must be positive")
        return int(count)

    @validator("duration_in_seconds")
    def duration_must_be_positive(cls, duration):
        if int(duration) <= 0:
            raise ValueError("duration must be positive")
        return int(duration)

class DistanceTravelledSchema(BaseModel):
    type: str
    username: str
    created_at: datetime
    distance_in_meters: int
    duration_in_seconds: int

    @validator("created_at", pre=True)
    def validate_created_at(cls, v):
        return datetime.fromisoformat(v.replace("Z", "+00:00"))

    @validator("type")
    def type_must_be_steps_taken(cls, type):
        if type != "steps_taken":
            raise ValueError("type must be steps_taken")
        return type

    @validator("distance_in_meters")
    def distance_must_be_positive(cls, distance_in_meters):
        if int(distance_in_meters) <= 0:
            raise ValueError("Distance must be positive")
        return int(distance_in_meters)

    @validator("duration_in_seconds")
    def duration_must_be_positive(cls, duration):
        if int(duration) <= 0:
            raise ValueError("duration must be positive")
        return int(duration)


MetricSchema = Union[ExerciseSetCompletedSchema, TrainingPlanCompletedSchema, StepsTakenSchema, DistanceTravelledSchema]
