import pytest

from src.infrastructure.goal.goal_schema import *

# Max weight lifted in exercise


def test_fails_if_missing_exercise_title():
    data = {
        "type": "max_weight_lifted_in_exercise",
        "username": "Martin",
        "goal_weight_in_kg": 100,
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2100-01-08T00:00:00Z",
    }

    with pytest.raises(TypeError):
        MaxWeightLiftedInExerciseSchema(data)


def test_fails_if_missing_goal_weight():
    data = {
        "type": "max_weight_lifted_in_exercise",
        "username": "Martin",
        "exercise_title": "Bench press",
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2100-01-08T00:00:00Z",
    }

    with pytest.raises(TypeError):
        MaxWeightLiftedInExerciseSchema(data)


def test_fails_if_goal_weight_is_negative():
    data = {
        "type": "max_weight_lifted_in_exercise",
        "username": "Martin",
        "exercise_title": "Bench press",
        "goal_weight_in_kg": -100,
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2100-01-08T00:00:00Z",
    }

    with pytest.raises(TypeError):
        MaxWeightLiftedInExerciseSchema(data)


def test_fails_if_deadline_is_before_start():
    data = {
        "type": "max_weight_lifted_in_exercise",
        "username": "Martin",
        "exercise_title": "Bench press",
        "goal_weight_in_kg": -100,
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2000-01-08T00:00:00Z",
    }

    with pytest.raises(TypeError):
        MaxWeightLiftedInExerciseSchema(data)


def test_fails_if_type_is_not_max_weight_lifted_in_exercise():
    data = {
        "type": "max_weight",
        "username": "Martin",
        "exercise_title": "Bench press",
        "goal_weight_in_kg": 100,
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2000-01-08T00:00:00Z",
    }

    with pytest.raises(TypeError):
        MaxWeightLiftedInExerciseSchema(data)


def test_max_weight_fails_if_no_username():
    data = {
        "type": "max_weight",
        "exercise_title": "Bench press",
        "goal_weight_in_kg": 100,
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2023-01-01T00:00:00Z",
    }

    with pytest.raises(TypeError):
        MaxWeightLiftedInExerciseSchema(data)


def test_max_weight_fails_if_starting_date_is_wrong():
    data = {
        "type": "max_weight",
        "exercise_title": "Bench press",
        "goal_weight_in_kg": 100,
        "starting_date": "oa",
        "deadline": "2023-01-01T00:00:00Z",
    }

    with pytest.raises(TypeError):
        MaxWeightLiftedInExerciseSchema(data)


def test_max_weight_fails_if_deadline_is_wrong():
    data = {
        "type": "max_weight",
        "exercise_title": "Bench press",
        "goal_weight_in_kg": 100,
        "deadline": "oa",
        "starting_date": "2023-01-01T00:00:00Z",
    }

    with pytest.raises(TypeError):
        MaxWeightLiftedInExerciseSchema(data)


# Total Steps taken


def test_fails_if_missing_goal_num_of_steps():
    data = {
        "type": "total_steps_taken",
        "username": "Martin",
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2100-01-08T00:00:00Z",
    }

    with pytest.raises(TypeError):
        TotalStepsTakenSchema(data)


def test_fails_if_goal_num_of_steps_is_negative():
    data = {
        "type": "total_steps_taken",
        "username": "Martin",
        "goal_num_of_steps": -100,
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2100-01-08T00:00:00Z",
    }

    with pytest.raises(TypeError):
        TotalStepsTakenSchema(data)


def test_steps_fails_if_no_username():
    data = {
        "type": "total_steps_taken",
        "goal_num_of_steps": 100,
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2100-01-08T00:00:00Z",
    }

    with pytest.raises(TypeError):
        TotalStepsTakenSchema(data)


def test_steps_fails_if_deadline_is_before_start():
    data = {
        "type": "total_steps_taken",
        "username": "Martin",
        "goal_num_of_steps": 100,
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2000-01-08T00:00:00Z",
    }

    with pytest.raises(TypeError):
        TotalStepsTakenSchema(data)


def test_steps_fails_if_deadline_is_wrong():
    data = {
        "type": "total_steps_taken",
        "username": "Martin",
        "goal_num_of_steps": 100,
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "ss",
    }

    with pytest.raises(TypeError):
        TotalStepsTakenSchema(data)


def test_steps_fails_if_starting_date_is_wrong():
    data = {
        "type": "total_steps_taken",
        "username": "Martin",
        "goal_num_of_steps": 100,
        "deadline": "2021-01-01T00:00:00Z",
        "starting_date": "ss",
    }

    with pytest.raises(TypeError):
        TotalStepsTakenSchema(data)


# Total distance travelled

def test_fails_is_missing_goal_distance():
    data = {
        "type": "total_distance_travelled",
        "username": "Martin",
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2100-01-08T00:00:00Z",
    }

    with pytest.raises(TypeError):
        TotalDistanceTravelledSchema(data)


def test_fails_if_goal_distance_is_negative():
    data = {
        "type": "total_distance_travelled",
        "username": "Martin",
        "goal_distance_in_meters": -100,
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "2100-01-08T00:00:00Z",
    }

    with pytest.raises(TypeError):
        TotalDistanceTravelledSchema(data)

def test_distance_fails_if_deadline_is_wrong():
    data = {
        "type": "total_distance_travelled",
        "username": "Martin",
        "goal_distance_in_meters": 100,
        "starting_date": "2021-01-01T00:00:00Z",
        "deadline": "ss",
    }

    with pytest.raises(TypeError):
        TotalDistanceTravelledSchema(data)


def test_distance_fails_if_starting_date_is_wrong():
    data = {
        "type": "total_distance_travelled",
        "username": "Martin",
        "goal_distance_in_meters": 100,
        "deadline": "2021-01-01T00:00:00Z",
        "starting_date": "ss",
    }

    with pytest.raises(TypeError):
        TotalDistanceTravelledSchema(data)
