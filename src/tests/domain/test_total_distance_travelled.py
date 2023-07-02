import sys
sys.path.append('/app/src')

from src.domain.goal.distance_travelled import TotalDistanceTravelled


from datetime import datetime, timedelta

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

    goal = TotalDistanceTravelled(goal_dict, metric_factory)

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
        "goal_distance_in_meters": 3000,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    goal = TotalDistanceTravelled(goal_dict, metric_factory)

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
        "goal_distance_in_meters": 4000,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    goal = TotalDistanceTravelled(goal_dict, metric_factory)

    # Then
    assert goal.completion_percentage() == 100 * 2000 / 4000


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

    goal = TotalDistanceTravelled(goal_dict, metric_factory)

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
        "goal_distance_in_meters": 1500,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    goal = TotalDistanceTravelled(goal_dict, metric_factory)

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
        "goal_distance_in_meters": 3000,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    goal = TotalDistanceTravelled(goal_dict, metric_factory)

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
        "goal_distance_in_meters": 3000,
        "starting_date": starting_date,
        "deadline": deadline,
        "metrics": metrics,
    }

    goal = TotalDistanceTravelled(goal_dict, metric_factory)

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

    goal = TotalDistanceTravelled(goal_dict, metric_factory)

    # Then
    assert not goal.was_failed()
