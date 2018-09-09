from .gmk_board_02 import Board
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


def test_place_piece(fresh_board):
    fresh_board.stone = 1
    fresh_board.place_piece(0, 0)
    assert fresh_board.board[0][0] == fresh_board.stone


def test_placeover_error(fresh_board):
    fresh_board.stone = 1
    fresh_board.place_piece(0, 0)
    assert fresh_board.place_piece(0, 0) == IndexError
