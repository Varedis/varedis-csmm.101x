#!/usr/bin/env python
"""
Script for solving an 8 puzzle in BFS, DFS and A*

Example command: python driver.py bfs 1,0,4,2,3,5,7,6,8
"""

import resource
import sys
import time

from state import State
from bfs import BFS
from dfs import DFS

SEARCH_TYPE = sys.argv[1]
INITIAL_STATE = map(int, sys.argv[2].split(','))

game = State(INITIAL_STATE);

search = None

if SEARCH_TYPE == 'bfs':
    search = BFS(game)
if SEARCH_TYPE == 'dfs':
    search = DFS(game)

result = search.perform_search()
goal_pos = result.position

res = resource.getrusage(resource.RUSAGE_SELF)

def trace_path(goal_pos):
    pos = goal_pos
    path = []

    while pos != None:
        if (pos.node.action != None):
            path.append(pos.node.action)
        pos = pos.prev

    return path[::-1]

start_time = time.time()

f = open('output.txt', 'w')
f.write('path_to_goal: %s\n' % trace_path(goal_pos))
f.write('cost_of_path: %d\n' % goal_pos.cost)
f.write('nodes_expanded: %d\n' % result.nodes_expanded)
f.write('search_depth: %d\n' % goal_pos.depth)
f.write('max_search_depth: %d\n' % result.max_depth)
f.write('running_time: %f\n' % (time.time() - start_time))
f.write('max_ram_usage: %f\n' % (res.ru_maxrss /1024 / 1024))
f.close()
