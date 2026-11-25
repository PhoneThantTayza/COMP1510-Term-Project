from rock_paper_scissors import get_rounds

from rock_paper_scissors import decide_win_lose_each_round


def test_player_wins():
    assert decide_win_lose_each_round("rock", "scissor") == "win"
    assert decide_win_lose_each_round("paper", "rock") == "win"
    assert decide_win_lose_each_round("scissor", "paper") == "win"


def test_player_loses():
    assert decide_win_lose_each_round("rock", "paper") == "lose"
    assert decide_win_lose_each_round("paper", "scissor") == "lose"
    assert decide_win_lose_each_round("scissor", "rock") == "lose"


def test_matching_choices_tie():
    assert decide_win_lose_each_round("rock", "rock") == "tie"
    assert decide_win_lose_each_round("paper", "paper") == "tie"
    assert decide_win_lose_each_round("scissor", "scissor") == "tie"
