from .gmk_board import Board
import pytest


@pytest.fixture
def fresh_board():
    return Board()


def test_board_instance(fresh_board):
    assert fresh_board


def test_board_id(fresh_board):
    uuid = fresh_board.game_id
    assert uuid


def test_board_moves_list(fresh_board):
    moves = fresh_board.moves
    assert moves == []