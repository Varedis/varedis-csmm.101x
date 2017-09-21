class Board:
    def __init__(self, initialState):
        self.initialState = initialState

    def resolveState(self, state, action):
        print state
        print action
        blank_pos = state.index(0)

        print blank_pos

        if action == 'UP':
            if blank_pos in [0, 1, 2]:
                print 'Can\'t go up'
                return

            print 'COULD GO UP'
            return

        if action == 'DOWN':
            if blank_pos in [6, 7, 8]:
                print 'Can\'t go down'
                return
                
            print 'COULD GO DOWN'
            return

        if action == 'LEFT':
            if blank_pos in [0, 3, 6]:
                print 'Can\'t go left'
                return

            print 'COULD GO LEFT'
            return

        if action == 'RIGHT':
            if blank_pos in [2, 5, 8]:
                print 'Can\'t go right'
                return

            print 'COULD GO RIGHT'
            return
