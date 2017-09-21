#!/usr/bin/env python
"""
Script for solving an 8 puzzle in BFS, DFS and A*

Example command: python driver.py bfs 1,0,4,2,3,5,7,6,8
"""

import sys
import resource

from state import State
from bfs import BFS

SEARCH_TYPE = sys.argv[1]
INITIAL_STATE = map(int, sys.argv[2].split(','))

print SEARCH_TYPE
print INITIAL_STATE

game = State(INITIAL_STATE);

bfs = BFS(game)
bfs.perform_search()

game.expand()

res = resource.getrusage(resource.RUSAGE_SELF)

f = open('output.txt', 'w')
f.write('path_to_goal: %s\n' % '[1,2,3]')
f.write('cost_of_path: %d\n' % 3)
f.write('nodes_expanded: %d\n' % 10)
f.write('search_depth: %d\n' % 3)
f.write('max_search_depth: %d\n' % 4)
f.write('running_time: %f\n' % res.ru_utime)
f.write('max_ram_usage: %f\n' % res.ru_maxrss)
f.close()
