from collections import namedtuple

from search import Search

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

class DFS(Search):
    def __init__(self, start):
        Search.__init__(self, start)
        self.fringe = Stack()
        
    def initialise(self):
        self.SearchPos = namedtuple('SearchPos', 'node, cost, depth, prev')
        position = self.SearchPos(self.start, 0, 0, None)
        self.fringe.push(position)
        self.expanded.add(str(self.start))

    def perform_search(self):
        self.initialise()

        max_depth = 0

        while not self.fringe.isEmpty():
            position = self.fringe.pop()
            node = position.node

            if self.goal_test(node):
                Success = namedtuple('Success', 'position, max_depth, nodes_expanded')
                success = Success(position, max_depth, len(self.explored))
                return success

            self.explored.add(str(node))

            for child in self.expandSuccessors(node)[::-1]:
                in_fringe = str(child) in self.explored

                if str(child) not in self.expanded and not in_fringe:
                    self.expanded.add(str(child))
    
                    depth = position.depth + 1
                    if max_depth < depth:
                        max_depth = depth
                    
                    child_position = self.SearchPos(child, position.cost + 1, depth, position)
                    self.fringe.push(child_position)
