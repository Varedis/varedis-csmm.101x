"""
Handles the state of world
"""

from board import Board

class State(object):
    """
    Class for accessing the current state
    """
    
    def __init__(self, initialState):
        self.initial_state = initialState
        self.board = Board(initialState)
        self.action = None

    def __eq__(self, other):
        return self.board == other.board

    def __str__(self):
        return str(self.board)

    def __hash__(self):
        return hash(str(self))

    def expand(self):
        return [
            self.perform_action('Up'),
            self.perform_action('Down'),
            self.perform_action('Left'),
            self.perform_action('Right'),
        ]

    def perform_action(self, action):
        state = self.board.resolve_state(action)
        if state is not None:
            new_state = State(state)
            new_state.action = action
            return new_state
        else:
            return self
        