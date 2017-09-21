class Search(object):
    def goal_test(self, state):
        return str(state) == str(range(0, 9))
