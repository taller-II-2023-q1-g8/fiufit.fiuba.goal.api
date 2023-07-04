import pytest
from datetime import datetime, timedelta

from src.infrastructure.metric.metric_factory import MetricFactory

from src.infrastructure.goal.goal_factory import GoalFactory
from src.domain.goal.max_weight_lifted_in_exercise import MaxWeightLiftedInExercise
from src.domain.goal.steps_taken import TotalStepsTaken
from src.domain.goal.training_plan_completion import TrainingPlanCompletion
from src.domain.goal.distance_travelled import TotalDistanceTravelled

def test_max_weight_lifted_in_exercise_is_created():
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        {
            "username": "Martin",
            "type": "exercise_set_completed",
            "created_at": date1,
            "exercise_title": "Bench Press",
            "weight_in_kg": 110,
            "reps": 10,
        },
        {
            "username": "Martin",
            "type": "exercise_set_completed",
            "created_at": date2,
            "exercise_title": "Bench Press",
            "weight_in_kg": 110,
            "reps": 10,
        },
    ]


    goal_dict = {
        "_id": None,
        "username": "Martin",
        "type": "max_weight_lifted_in_exercise",
        "goal_weight_in_kg": 110,
        "exercise_title": "Bench Press",
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    factory = GoalFactory(metric_factory)
    goal = factory.from_dict(goal_dict)
    assert isinstance(goal, MaxWeightLiftedInExercise)

def test_total_steps_taken_is_created():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        {
            "username": "Martin",
            "type": "steps_taken",
            "created_at": date1,
            "duration_in_seconds": 120,
            "step_count": 100
        },
        {
            "username": "Martin",
            "type": "steps_taken",
            "created_at": date2,
            "duration_in_seconds": 180,
            "step_count": 100
        },

    ]

    goal_dict = {
        "_id": None,
        "username": "Martin",
        "type": "total_steps_taken",
        "goal_num_of_steps": 200,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    factory = GoalFactory(metric_factory)
    goal = factory.from_dict(goal_dict)

    # Then
    assert isinstance(goal, TotalStepsTaken)

def total_distance_travelled_is_created():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        {
            "username": "Martin",
            "type": "distance_travelled",
            "created_at": date1,
            "duration_in_seconds": 120,
            "distance_in_meters": 1000
        },
        {
            "username": "Martin",
            "type": "distance_travelled",
            "created_at": date2,
            "duration_in_seconds": 180,
            "distance_in_meters": 1000
        },

    ]

    goal_dict = {
        "_id": None,
        "username": "Martin",
        "type": "total_distance_travelled",
        "goal_distance_in_meters": 2000,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    factory = GoalFactory(metric_factory)
    goal = factory.from_dict(goal_dict)

    # Then
    assert isinstance(goal, TotalDistanceTravelled)

def test_training_plan_completion_is_created():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)
    date3 = date2 + timedelta(minutes=2)

    metrics = [
        {
            "username": "Martin",
            "type": "training_plan_completed",
            "created_at": date1,
            "plan_title": "Plan 1",
        },
        {
            "username": "Martin",
            "type": "training_plan_completed",
            "created_at": date2,
            "plan_title": "Plan 1",
        },
        {
            "username": "Martin",
            "type": "training_plan_completed",
            "created_at": date3,
            "plan_title": "Plan 1",
        },
    ]

    goal_dict = {
        "username": "Martin",
        "_id": None,
        "type": "training_plan_completion",
        "goal_num_of_completions": 3,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    factory = GoalFactory(metric_factory)
    goal = factory.from_dict(goal_dict)

    # Then
    assert isinstance(goal, TrainingPlanCompletion)


def test_nonexistant_goal_type_raises_error():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)
    date3 = date2 + timedelta(minutes=2)

    metrics = []

    goal_dict = {
        "username": "Martin",
        "_id": None,
        "type": "random",
        "goal_num_of_completions": 3,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    factory = GoalFactory(metric_factory)

    # Then
    with pytest.raises(ValueError):
        goal = factory.from_dict(goal_dict)