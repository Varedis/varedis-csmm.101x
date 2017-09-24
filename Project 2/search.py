class Search(object):
    def __init__(self, start):
        self.start = start
        self.explored = set()
        self.expanded = set()

    def initialise(self):
        return

    def goal_test(self, state):    
        return str(state) == str(range(0, 9))

    def expandSuccessors(self, node):
        return node.expand()
