class Board(object):
    def __init__(self, state):
        self.state = state

    def resolve_state(self, action):
        print self.state
        print action
        blank_pos = self.state.index(0)

        print blank_pos

        if action == 'UP':
            if blank_pos in [0, 1, 2]:
                return None

            new_list = list(self.state)
            new_list[blank_pos], new_list[blank_pos - 3] = new_list[blank_pos - 3], new_list[blank_pos]
            return new_list

        if action == 'DOWN':
            if blank_pos in [6, 7, 8]:
                return None

            new_list = list(self.state)
            new_list[blank_pos], new_list[blank_pos + 3] = new_list[blank_pos + 3], new_list[blank_pos]
            return new_list

        if action == 'LEFT':
            if blank_pos in [0, 3, 6]:
                return None

            new_list = list(self.state)
            new_list[blank_pos], new_list[blank_pos - 1] = new_list[blank_pos - 1], new_list[blank_pos]
            return new_list

        if action == 'RIGHT':
            if blank_pos in [2, 5, 8]:
                return None

            new_list = list(self.state)
            new_list[blank_pos], new_list[blank_pos + 1] = new_list[blank_pos + 1], new_list[blank_pos]
            return new_list
