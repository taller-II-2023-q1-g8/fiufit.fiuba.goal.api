from datetime import datetime, timedelta

from src.domain.goal.max_weight_lifted_in_exercise\
    import MaxWeightLiftedInExercise
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
            'type': 'exercise_set_completed',
            'created_at': date1,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        },
        {
            'type': 'exercise_set_completed',
            'created_at': date2,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        }
    ]

    goal_dict = {
        '_id': None,
        'username': 'Martin',
        'type': 'max_weight_lifted_in_exercise',
        'goal_weight_in_kg': 110,
        'exercise_title': "Bench Press",
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = MaxWeightLiftedInExercise(goal_dict, metric_factory)

    # Then
    assert goal.was_completed()


def test_is_not_completed_when_unsatisfied():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        {
            'type': 'exercise_set_completed',
            'created_at': date1,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        },
        {
            'type': 'exercise_set_completed',
            'created_at': date2,
            'exercise_title': "Bench Press",
            'weight_in_kg': 90,
            'reps': 10
        }
    ]

    goal_dict = {
        '_id': None,
        'username': 'Martin',
        'type': 'max_weight_lifted_in_exercise',
        'goal_weight_in_kg': 120,
        'exercise_title': "Bench Press",
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = MaxWeightLiftedInExercise(goal_dict, metric_factory)

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
            'type': 'exercise_set_completed',
            'created_at': date1,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        },
        {
            'type': 'exercise_set_completed',
            'created_at': date2,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        }
    ]

    goal_dict = {
        '_id': None,
        'username': 'Martin',
        'type': 'max_weight_lifted_in_exercise',
        'goal_weight_in_kg': 130,
        'exercise_title': "Bench Press",
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = MaxWeightLiftedInExercise(goal_dict, metric_factory)

    # Then
    assert goal.completion_percentage() == 100 * 110/130


def test_completion_progress_full():
    # Given
    metric_factory = MetricFactory()
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        {
            'type': 'exercise_set_completed',
            'created_at': date1,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        },
        {
            'type': 'exercise_set_completed',
            'created_at': date2,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        }
    ]

    goal_dict = {
        '_id': None,
        'username': 'Martin',
        'type': 'max_weight_lifted_in_exercise',
        'goal_weight_in_kg': 110,
        'exercise_title': "Bench Press",
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = MaxWeightLiftedInExercise(goal_dict, metric_factory)

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
            'type': 'exercise_set_completed',
            'created_at': date1,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        },
        {
            'type': 'exercise_set_completed',
            'created_at': date2,
            'exercise_title': "Bench Press",
            'weight_in_kg': 150,
            'reps': 10
        }
    ]

    goal_dict = {
        '_id': None,
        'username': 'Martin',
        'type': 'max_weight_lifted_in_exercise',
        'goal_weight_in_kg': 110,
        'exercise_title': "Bench Press",
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = MaxWeightLiftedInExercise(goal_dict, metric_factory)

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
            'type': 'exercise_set_completed',
            'created_at': date1,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        },
        {
            'type': 'exercise_set_completed',
            'created_at': date2,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        }
    ]

    goal_dict = {
        '_id': None,
        'username': 'Martin',
        'type': 'max_weight_lifted_in_exercise',
        'goal_weight_in_kg': 120,
        'exercise_title': "Bench Press",
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = MaxWeightLiftedInExercise(goal_dict, metric_factory)

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
            'type': 'exercise_set_completed',
            'created_at': date1,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        },
        {
            'type': 'exercise_set_completed',
            'created_at': date2,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        }
    ]

    goal_dict = {
        '_id': None,
        'username': 'Martin',
        'type': 'max_weight_lifted_in_exercise',
        'goal_weight_in_kg': 120,
        'exercise_title': "Bench Press",
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = MaxWeightLiftedInExercise(goal_dict, metric_factory)

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
            'type': 'exercise_set_completed',
            'created_at': date1,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        },
        {
            'type': 'exercise_set_completed',
            'created_at': date2,
            'exercise_title': "Bench Press",
            'weight_in_kg': 110,
            'reps': 10
        }
    ]

    goal_dict = {
        '_id': None,
        'username': 'Martin',
        'type': 'max_weight_lifted_in_exercise',
        'goal_weight_in_kg': 110,
        'exercise_title': "Bench Press",
        'starting_date': starting_date,
        'deadline': deadline,
        'metrics': metrics
    }

    goal = MaxWeightLiftedInExercise(goal_dict, metric_factory)

    # Then
    assert not goal.was_failed()
