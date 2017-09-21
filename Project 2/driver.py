#!/usr/bin/env python
"""
Script for solving an 8 puzzle in BFS, DFS and A*

Example command: python driver.py bfs 1,0,4,2,3,5,7,6,8
"""

import sys

from state import State

SEARCH_TYPE = sys.argv[1]
INITIAL_STATE = map(int, sys.argv[2].split(','))

print SEARCH_TYPE
print INITIAL_STATE

state = State(SEARCH_TYPE, INITIAL_STATE);

state.expand()
