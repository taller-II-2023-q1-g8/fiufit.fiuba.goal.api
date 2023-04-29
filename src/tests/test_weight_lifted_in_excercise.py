from datetime import datetime, timedelta

from src.domain.goal.max_weight_lifted_in_excercise import MaxWeightLiftedInExcercise
from src.domain.metric.metric import ExcerciseSetCompleted


def test_is_completed_when_satisfied():
    # Given
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)
    date3 = datetime(2021, 1, 3)

    metrics = [
        ExcerciseSetCompleted(date1, "Martin", "Bench Press",
                              weight_in_kg=110, reps=10),
        ExcerciseSetCompleted(date2, "Martin", "Bench Press",
                              weight_in_kg=110, reps=7),
        ExcerciseSetCompleted(date3, "Martin", "Bench Press",
                              weight_in_kg=100, reps=7),
    ]

    deadline = datetime(2100, 1, 1)
    goal = MaxWeightLiftedInExcercise(110, "Bench Press", deadline, "Martin", metrics)

    # Then
    assert goal.was_achieved()


def test_is_completed_when_unsatisfied():
    # Given
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)
    date3 = datetime(2021, 1, 3)

    metrics = [
        ExcerciseSetCompleted(date1, "Martin", "Bench Press",
                              weight_in_kg=110, reps=10),
        ExcerciseSetCompleted(date2, "Martin", "Bench Press",
                              weight_in_kg=110, reps=7),
        ExcerciseSetCompleted(date3, "Martin", "Bench Press",
                              weight_in_kg=100, reps=7),
    ]

    deadline = datetime(2100, 1, 1)
    goal = MaxWeightLiftedInExcercise(120, "Bench Press", deadline, "Martin", metrics)

    # Then
    assert not goal.was_achieved()


def test_completion_progress_not_full():
    # Given
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)
    date3 = datetime(2021, 1, 3)

    metrics = [
        ExcerciseSetCompleted(date1, "Martin", "Bench Press",
                              weight_in_kg=110, reps=10),
        ExcerciseSetCompleted(date2, "Martin", "Bench Press",
                              weight_in_kg=110, reps=7),
        ExcerciseSetCompleted(date3, "Martin", "Bench Press",
                              weight_in_kg=100, reps=7),
    ]

    deadline = datetime(2100, 1, 1)
    goal = MaxWeightLiftedInExcercise(180, "Bench Press", deadline, "Martin", metrics)

    # Then
    assert goal.completion_percentage() == 100 * 110/180


def test_completion_progress_full():
    # Given
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)
    date3 = datetime(2021, 1, 3)

    metrics = [
        ExcerciseSetCompleted(date1, "Martin", "Bench Press",
                              weight_in_kg=180, reps=10),
        ExcerciseSetCompleted(date2, "Martin", "Bench Press",
                              weight_in_kg=170, reps=7),
        ExcerciseSetCompleted(date3, "Martin", "Bench Press",
                              weight_in_kg=150, reps=7),
    ]

    deadline = datetime(2100, 1, 1)
    goal = MaxWeightLiftedInExcercise(180, "Bench Press", deadline, "Martin", metrics)

    # Then
    assert goal.completion_percentage() == 100


def test_completion_progress_overflow():
    # Given
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)
    date3 = datetime(2021, 1, 3)

    metrics = [
        ExcerciseSetCompleted(date1, "Martin", "Bench Press",
                              weight_in_kg=180, reps=10),
        ExcerciseSetCompleted(date2, "Martin", "Bench Press",
                              weight_in_kg=170, reps=7),
        ExcerciseSetCompleted(date3, "Martin", "Bench Press",
                              weight_in_kg=150, reps=7),
    ]

    deadline = datetime(2100, 1, 1)
    goal = MaxWeightLiftedInExcercise(150, "Bench Press", deadline, "Martin", metrics)

    # Then
    assert goal.completion_percentage() == 100


def test_was_failed_after_deadline_and_incomplete():
    # Given
    date1 = datetime(2020, 12, 31)
    date2 = date1 + timedelta(minutes=2)
    date3 = date2 + timedelta(minutes=2)

    metrics = [
        ExcerciseSetCompleted(date1, "Martin", "Bench Press",
                              weight_in_kg=100, reps=10),
        ExcerciseSetCompleted(date2, "Martin", "Bench Press",
                              weight_in_kg=100, reps=7),
        ExcerciseSetCompleted(date3, "Martin", "Bench Press",
                              weight_in_kg=70, reps=7),
    ]

    deadline = datetime(2021, 1, 1)
    goal = MaxWeightLiftedInExcercise(150, "Bench Press", deadline, "Martin", metrics)

    # Then
    assert goal.was_failed()


def test_was_not_failed_before_deadline():
    # Given
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)
    date3 = datetime(2021, 1, 3)

    metrics = [
        ExcerciseSetCompleted(date1, "Martin", "Bench Press",
                              weight_in_kg=100, reps=10),
        ExcerciseSetCompleted(date2, "Martin", "Bench Press",
                              weight_in_kg=100, reps=7),
        ExcerciseSetCompleted(date3, "Martin", "Bench Press",
                              weight_in_kg=70, reps=7),
    ]

    deadline = datetime(2100, 1, 1)
    goal = MaxWeightLiftedInExcercise(150, "Bench Press", deadline, "Martin", metrics)

    # Then
    assert not goal.was_failed()


def test_was_not_failed_after_deadline_but_completed():
    # Given
    date1 = datetime(2020, 12, 31)
    date2 = date1 + timedelta(minutes=2)
    date3 = date2 + timedelta(minutes=2)

    metrics = [
        ExcerciseSetCompleted(date1, "Martin", "Bench Press",
                              weight_in_kg=150, reps=10),
        ExcerciseSetCompleted(date2, "Martin", "Bench Press",
                              weight_in_kg=100, reps=7),
        ExcerciseSetCompleted(date3, "Martin", "Bench Press",
                              weight_in_kg=70, reps=7),
    ]

    deadline = datetime(2021, 1, 1)
    goal = MaxWeightLiftedInExcercise(150, "Bench Press", deadline, "Martin", metrics)

    # Then
    assert not goal.was_failed()

