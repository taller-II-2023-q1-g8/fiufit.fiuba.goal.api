from datetime import datetime

from src.domain.goal.training_plan_completion import TrainingPlanCompletion
from src.domain.metric.metric import TrainingPlanCompleted


def test_is_completed_when_satisfied():
    # Given
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)
    date3 = datetime(2021, 1, 3)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
        TrainingPlanCompleted(date3, "Martin", "Plan 1"),
    ]

    deadline = datetime(2100, 1, 1)
    goal = TrainingPlanCompletion(3, deadline, metrics)

    # Then
    assert goal.was_achieved()


def test_isnt_completed_when_not_satisfied():
    # Given
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
    ]

    deadline = datetime(2100, 1, 1)
    goal = TrainingPlanCompletion(3, deadline, metrics)

    # Then
    assert not goal.was_achieved()


def test_completion_progress_not_full():
    # Given
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
    ]

    deadline = datetime(2100, 1, 1)
    goal = TrainingPlanCompletion(3, deadline, metrics)

    # Then
    assert goal.completion_percentage() == 2/3


def test_completion_progress_full():
    # Given
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)
    date3 = datetime(2021, 1, 3)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
        TrainingPlanCompleted(date3, "Martin", "Plan 1"),
    ]

    deadline = datetime(2100, 1, 1)
    goal = TrainingPlanCompletion(3, deadline, metrics)

    # Then
    assert goal.completion_percentage() == 1.0


def test_completion_progress_overflow():
    # Given
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)
    date3 = datetime(2021, 1, 3)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
        TrainingPlanCompleted(date2, "Martin", "Plan 1"),
        TrainingPlanCompleted(date3, "Martin", "Plan 1"),
    ]

    deadline = datetime(2100, 1, 1)
    goal = TrainingPlanCompletion(2, deadline, metrics)

    # Then
    assert goal.completion_percentage() == 1.0


def test_was_failed_after_deadline_and_incomplete():
    # Given
    date1 = datetime(2021, 1, 1)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
    ]

    expired_date = datetime(2021, 1, 2)
    goal = TrainingPlanCompletion(
        3,
        deadline=expired_date,
        metrics=metrics
        )

    # Then
    assert goal.was_failed()


def test_was_not_failed_before_deadline():
    # Given
    date1 = datetime(2021, 1, 1)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
    ]

    deadline = datetime(2200, 1, 2)
    goal = TrainingPlanCompletion(
        3,
        deadline,
        metrics=metrics
        )

    # Then
    assert not goal.was_failed()


def test_was_not_failed_after_deadline_but_completed():
        # Given
    date1 = datetime(2021, 1, 1)

    metrics = [
        TrainingPlanCompleted(date1, "Martin", "Plan 1"),
    ]

    deadline = datetime(2020, 1, 2)
    goal = TrainingPlanCompletion(
        1,
        deadline,
        metrics=metrics
        )

    # Then
    assert not goal.was_failed()
