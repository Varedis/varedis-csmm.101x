from search import Search

class BFS(Search):
    def __init__(self, start):
        self.start = start

    def perform_search(self):
        print self.goal_test(self.start);
