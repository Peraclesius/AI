import pytest
from tikctactoe import *

def test_finds_successor():
    assert successor(INITIAL_STATE, 1, 'X') == '.X.......'

def test_finds_legal_moves():
    assert legal_moves('.X...O...') == [0, 2, 3, 4, 6, 7, 8]

def test_finds_win_for_x():
    assert winner('...XXX.OO') == 1

def test_finds_win_for_o():
    assert winner('...XX.OOO') == -1

def test_finds_value_at_end_of_game():
    assert value('...XXX.OO', 'O', less, 2) == 1
    assert value('...XXX.OO', 'X', greater, -2) == 1

def test_finds_win_in_one_move():
    assert value('XX....O.O', 'X', greater, -2) == 1

def test_finds_value_after_two_moves():
    assert value('XOXXXOO..', 'O', less, 2) == 0

def test_finds_value_after_three_moves():
    assert value('.X.X.O.O.', 'X', greater, -2) == 1
    assert value('.X.X.O.O.', 'O', less, 2) == -1

def test_finds_best_move_depth_1():
    assert best_move_for_x('XX.O....O')

def test_finds_best_move_deep():
    assert best_move_for_x('X..OO...X') == 5

