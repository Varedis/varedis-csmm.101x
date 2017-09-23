import Queue
from collections import namedtuple

from search import Search

class BFS(Search):
    def __init__(self, start):
        Search.__init__(self, start)
        self.fringe = Queue.Queue()
        
    def initialise(self):
        self.SearchPos = namedtuple('SearchPos', 'node, cost, depth, prev')
        position = self.SearchPos(self.start, 0, 0, None)
        self.fringe.put(position)

    def perform_search(self):
        self.initialise()

        max_depth = 0

        while not self.fringe.empty():
            position = self.fringe.get()
            node = position.node

            if self.goal_test(node):
                Success = namedtuple('Success', 'position, max_depth, nodes_expanded')
                success = Success(position, max_depth, len(self.explored))
                return success

            self.explored.add(str(node))

            for child in self.expandSuccessors(node):
                if str(child) not in self.explored:
                    depth = position.depth + 1
                    if max_depth < depth:
                        max_depth = depth
                    
                    child_position = self.SearchPos(child, position.cost + 1, depth, position)
                    self.fringe.put(child_position)
