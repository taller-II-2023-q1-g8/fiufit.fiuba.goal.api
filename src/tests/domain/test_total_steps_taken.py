import sys

sys.path.append('/app/src')

from datetime import datetime, timedelta

from src.domain.goal.steps_taken import TotalStepsTaken
from src.infrastructure.metric.metric_factory import MetricFactory


def test_is_completed_when_satisfied():
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

    goal = TotalStepsTaken(goal_dict, metric_factory)

    # Then
    assert goal.was_completed()


def test_is_not_completed_when_unsatisfied():
#     # Given
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
        "goal_num_of_steps": 201,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    goal = TotalStepsTaken(goal_dict, metric_factory)

    # Then
    assert not goal.was_completed()


def test_completion_progress_not_full():
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
        "goal_num_of_steps": 201,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    goal = TotalStepsTaken(goal_dict, metric_factory)

    # Then
    assert goal.completion_percentage() == 100 * 200 / 201


def test_completion_progress_full():
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

    goal = TotalStepsTaken(goal_dict, metric_factory)

    # Then
    assert goal.completion_percentage() == 100


def test_completion_progress_overflow():
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
        "goal_num_of_steps": 100,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    goal = TotalStepsTaken(goal_dict, metric_factory)

    # Then
    assert goal.completion_percentage() == 100


def test_was_failed_after_deadline_and_incomplete():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2021, 1, 4)
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
        "goal_num_of_steps": 201,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    goal = TotalStepsTaken(goal_dict, metric_factory)

    # Then
    assert goal.was_failed()


def test_was_not_failed_before_deadline():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2120, 1, 4)
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
        "goal_num_of_steps": 201,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    goal = TotalStepsTaken(goal_dict, metric_factory)

    # Then
    assert not goal.was_failed()


def test_was_not_failed_after_deadline_but_completed():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2021, 1, 4)
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

    goal = TotalStepsTaken(goal_dict, metric_factory)

    # Then
    assert not goal.was_failed()
