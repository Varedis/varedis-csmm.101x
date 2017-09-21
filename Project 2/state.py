"""
Handles the state of world
"""

from board import Board

GOAL_STATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]

class State(object):
    """
    Class for accessing the current state
    """
    
    def __init__(self, searchMethod, initialState):
        self.search_method = searchMethod
        self.initial_state = initialState
        self.board = Board(initialState)

    def expand(self):
        self.board.resolveState(self.initial_state, 'UP')
        self.board.resolveState(self.initial_state, 'DOWN')
        self.board.resolveState(self.initial_state, 'LEFT')
        self.board.resolveState(self.initial_state, 'RIGHT')