"""Completed learner tests for Week 12."""

import pytest
from exercises.decision import LOCAL_ACTIONS, choose_action, validate_turn


def test_normal_case() -> None:
    action = choose_action(1, 4)
    assert action == "right"
    assert action in LOCAL_ACTIONS


def test_edge_case_at_goal() -> None:
    assert choose_action(4, 4) == "wait"


def test_invalid_turn() -> None:
    with pytest.raises(ValueError, match="positive"):
        validate_turn(0)


def test_regression_position_past_goal_moves_left() -> None:
    assert choose_action(4, 1) == "left"
