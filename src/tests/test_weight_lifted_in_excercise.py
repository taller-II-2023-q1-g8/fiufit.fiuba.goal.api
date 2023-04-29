from datetime import datetime, timedelta

from src.domain.goal.max_weight_lifted_in_excercise\
    import MaxWeightLiftedInExcercise
from src.domain.metric.metric import ExcerciseSetCompleted


def test_is_completed_when_satisfied():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        ExcerciseSetCompleted(
            created_at=date1,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=110,
            reps=10),
        ExcerciseSetCompleted(
            created_at=date2,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=110,
            reps=9),
    ]

    goal = MaxWeightLiftedInExcercise(
        goal_weight_in_kg=110,
        excercise_title="Bench Press",
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics
    )

    # Then
    assert goal.was_achieved()


def test_is_not_completed_when_unsatisfied():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        ExcerciseSetCompleted(
            created_at=date1,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=110,
            reps=10),
        ExcerciseSetCompleted(
            created_at=date2,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=110,
            reps=9),
    ]

    goal = MaxWeightLiftedInExcercise(
        goal_weight_in_kg=120,
        excercise_title="Bench Press",
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics
    )

    # Then
    assert not goal.was_achieved()


def test_completion_progress_not_full():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        ExcerciseSetCompleted(
            created_at=date1,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=110,
            reps=10),
        ExcerciseSetCompleted(
            created_at=date2,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=110,
            reps=9),
    ]

    goal = MaxWeightLiftedInExcercise(
        goal_weight_in_kg=130,
        excercise_title="Bench Press",
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics
    )

    # Then
    assert goal.completion_percentage() == 100 * 110/130


def test_completion_progress_full():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        ExcerciseSetCompleted(
            created_at=date1,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=110,
            reps=10),
        ExcerciseSetCompleted(
            created_at=date2,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=120,
            reps=9),
    ]

    goal = MaxWeightLiftedInExcercise(
        goal_weight_in_kg=120,
        excercise_title="Bench Press",
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics
    )

    # Then
    assert goal.completion_percentage() == 100


def test_completion_progress_overflow():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        ExcerciseSetCompleted(
            created_at=date1,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=110,
            reps=10),
        ExcerciseSetCompleted(
            created_at=date2,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=150,
            reps=9),
    ]

    goal = MaxWeightLiftedInExcercise(
        goal_weight_in_kg=120,
        excercise_title="Bench Press",
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics
    )

    # Then
    assert goal.completion_percentage() == 100


def test_was_failed_after_deadline_and_incomplete():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2021, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        ExcerciseSetCompleted(
            created_at=date1,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=110,
            reps=10),
        ExcerciseSetCompleted(
            created_at=date2,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=120,
            reps=9),
    ]

    goal = MaxWeightLiftedInExcercise(
        goal_weight_in_kg=130,
        excercise_title="Bench Press",
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics
    )

    # Then
    assert goal.was_failed()


def test_was_not_failed_before_deadline():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2100, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        ExcerciseSetCompleted(
            created_at=date1,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=110,
            reps=10),
        ExcerciseSetCompleted(
            created_at=date2,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=120,
            reps=9),
    ]

    goal = MaxWeightLiftedInExcercise(
        goal_weight_in_kg=130,
        excercise_title="Bench Press",
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics
    )

    # Then
    assert not goal.was_failed()


def test_was_not_failed_after_deadline_but_completed():
    # Given
    starting_date = datetime(2021, 1, 1)
    deadline = datetime(2021, 1, 8)
    date1 = datetime(2021, 1, 2)
    date2 = date1 + timedelta(minutes=2)

    metrics = [
        ExcerciseSetCompleted(
            created_at=date1,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=110,
            reps=10),
        ExcerciseSetCompleted(
            created_at=date2,
            username="Martin",
            excercise_title="Bench Press",
            weight_in_kg=120,
            reps=9),
    ]

    goal = MaxWeightLiftedInExcercise(
        goal_weight_in_kg=120,
        excercise_title="Bench Press",
        starting_date=starting_date,
        deadline=deadline,
        username="Martin",
        metrics=metrics
    )

    # Then
    assert not goal.was_failed()
