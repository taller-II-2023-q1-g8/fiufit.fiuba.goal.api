from datetime import datetime, timedelta
from src.domain.goal.training_plan_completion import TrainingPlanCompletion
from src.infrastructure.metric.metric_factory import MetricFactory


def test_is_completed_when_satisfied():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)
    date3 = date2 + timedelta(minutes=2)

    metrics = [
        {
            'type': 'training_plan_completed',
            'created_at': date1, 
            'plan_title': "Plan 1"
        },
        {
            'type': 'training_plan_completed',
            'created_at': date2, 
            'plan_title': "Plan 1"
        },
        {
            'type': 'training_plan_completed',
            'created_at': date3, 
            'plan_title': "Plan 1"
        }
    ]

    goal_dict = {
        'username': 'Martin',
        '_id': None,
        'type': 'training_plan_completion',
        'goal_num_of_completions': 3,
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = TrainingPlanCompletion(goal_dict, metric_factory)

    # Then
    assert goal.was_completed()


def test_isnt_completed_when_not_satisfied():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        {
            'type': 'training_plan_completed',
            'created_at': date1, 
            'plan_title': "Plan 1"
        },
        {
            'type': 'training_plan_completed',
            'created_at': date2, 
            'plan_title': "Plan 1"
        }
    ]

    goal_dict = {
        'username': 'Martin',
        '_id': None,
        'type': 'training_plan_completion',
        'goal_num_of_completions': 3,
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = TrainingPlanCompletion(goal_dict, metric_factory)

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
            'type': 'training_plan_completed',
            'created_at': date1, 
            'plan_title': "Plan 1"
        },
        {
            'type': 'training_plan_completed',
            'created_at': date2, 
            'plan_title': "Plan 1"
        }
    ]

    goal_dict = {
        'username': 'Martin',
        '_id': None,
        'type': 'training_plan_completion',
        'goal_num_of_completions': 3,
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = TrainingPlanCompletion(goal_dict, metric_factory)

    # Then
    assert goal.completion_percentage() == 2/3 * 100


def test_completion_progress_full():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)
    date3 = date2 + timedelta(minutes=2)

    metrics = [
        {
            'type': 'training_plan_completed',
            'created_at': date1, 
            'plan_title': "Plan 1"
        },
        {
            'type': 'training_plan_completed',
            'created_at': date2, 
            'plan_title': "Plan 1"
        },
        {
            'type': 'training_plan_completed',
            'created_at': date3, 
            'plan_title': "Plan 1"
        }
    ]

    goal_dict = {
        'username': 'Martin',
        '_id': None,
        'type': 'training_plan_completion',
        'goal_num_of_completions': 3,
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = TrainingPlanCompletion(goal_dict, metric_factory)

    # Then
    assert goal.completion_percentage() == 100


def test_completion_progress_overflow():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)
    date3 = date2 + timedelta(minutes=2)

    metrics = [
        {
            'type': 'training_plan_completed',
            'created_at': date1,
            'plan_title': "Plan 1"
        },
        {
            'type': 'training_plan_completed',
            'created_at': date2,
            'plan_title': "Plan 1"
        },
        {
            'type': 'training_plan_completed',
            'created_at': date3,
            'plan_title': "Plan 1"
        }
    ]

    goal_dict = {
        'username': 'Martin',
        '_id': None,
        'type': 'training_plan_completion',
        'goal_num_of_completions': 2,
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = TrainingPlanCompletion(goal_dict, metric_factory)

    # Then
    assert goal.completion_percentage() == 100


def test_was_failed_after_deadline_and_incomplete():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2021, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        {
            'type': 'training_plan_completed',
            'created_at': date1, 
            'plan_title': "Plan 1"
        },
        {
            'type': 'training_plan_completed',
            'created_at': date2, 
            'plan_title': "Plan 1"
        }
    ]

    goal_dict = {
        'username': 'Martin',
        '_id': None,
        'type': 'training_plan_completion',
        'goal_num_of_completions': 3,
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = TrainingPlanCompletion(goal_dict, metric_factory)

    # Then
    assert goal.was_failed()


def test_was_not_failed_before_deadline():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(3000, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        {
            'type': 'training_plan_completed',
            'created_at': date1, 
            'plan_title': "Plan 1"
        },
        {
            'type': 'training_plan_completed',
            'created_at': date2, 
            'plan_title': "Plan 1"
        }
    ]

    goal_dict = {
        'username': 'Martin',
        '_id': None,
        'type': 'training_plan_completion',
        'goal_num_of_completions': 3,
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = TrainingPlanCompletion(goal_dict, metric_factory)

    # Then
    assert not goal.was_failed()


def test_was_not_failed_after_deadline_but_completed():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2021, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        {
            'type': 'training_plan_completed',
            'created_at': date1, 
            'plan_title': "Plan 1"
        },
        {
            'type': 'training_plan_completed',
            'created_at': date2, 
            'plan_title': "Plan 1"
        }
    ]

    goal_dict = {
        'username': 'Martin',
        '_id': None,
        'type': 'training_plan_completion',
        'goal_num_of_completions': 2,
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = TrainingPlanCompletion(goal_dict, metric_factory)

    # Then
    assert not goal.was_failed()
