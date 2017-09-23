class Board(object):
    def __init__(self, state):
        self.state = state

    def __eq__(self, other):
        return self.state == other.state

    def __str__(self):
        return str(self.state)

    def __hash__(self):
        return hash(str(self))

    def resolve_state(self, action):
        blank_pos = self.state.index(0)

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
