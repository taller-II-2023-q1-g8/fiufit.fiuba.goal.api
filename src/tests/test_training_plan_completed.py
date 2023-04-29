from datetime import datetime, timedelta

from src.domain.goal.training_plan_completion import TrainingPlanCompletion
from src.domain.metric.metric import TrainingPlanCompleted


def test_is_completed_when_satisfied():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)
    date3 = date2 + timedelta(minutes=2)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
        TrainingPlanCompleted(date3, "Martin", "Plan 1"),
    ]

    goal = TrainingPlanCompletion(
        goal_num_of_completions=3,
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics)

    # Then
    assert goal.was_achieved()


def test_isnt_completed_when_not_satisfied():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
    ]

    goal = TrainingPlanCompletion(
        goal_num_of_completions=3,
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics)

    # Then
    assert not goal.was_achieved()


def test_completion_progress_not_full():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
    ]

    goal = TrainingPlanCompletion(
        goal_num_of_completions=3,
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics)

    # Then
    assert goal.completion_percentage() == 2/3 * 100


def test_completion_progress_full():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)
    date3 = date2 + timedelta(minutes=2)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
        TrainingPlanCompleted(date3, "Martin", "Plan 1"),
    ]

    goal = TrainingPlanCompletion(
        goal_num_of_completions=3,
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics)

    # Then
    assert goal.completion_percentage() == 100


def test_completion_progress_overflow():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)
    date3 = date2 + timedelta(minutes=2)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
        TrainingPlanCompleted(date3, "Martin", "Plan 1"),
    ]

    goal = TrainingPlanCompletion(
        goal_num_of_completions=2,
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics)

    # Then
    assert goal.completion_percentage() == 100


def test_was_failed_after_deadline_and_incomplete():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2021, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
    ]

    goal = TrainingPlanCompletion(
        goal_num_of_completions=3,
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics)

    # Then
    assert goal.was_failed()


def test_was_not_failed_before_deadline():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(3000, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
    ]

    goal = TrainingPlanCompletion(
        goal_num_of_completions=3,
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics)

    # Then
    assert not goal.was_failed()


def test_was_not_failed_after_deadline_but_completed():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2021, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
    ]

    goal = TrainingPlanCompletion(
        goal_num_of_completions=2,
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics)

    # Then
    assert not goal.was_failed()
