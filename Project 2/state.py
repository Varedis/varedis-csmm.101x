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

    def expand(self):
        self.perform_action('UP')
        self.perform_action('DOWN')
        self.perform_action('LEFT')
        self.perform_action('RIGHT')

    def perform_action(self, action):
        state = self.board.resolve_state(action)
        if state is not None:
            print 'STATE AFTER %s' % state
            return State(state)
        else:
            return self
        