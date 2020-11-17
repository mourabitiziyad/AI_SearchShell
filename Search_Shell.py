# function names are successor_function, goal_test, and heuristic
from queue import Queue
import numpy as np
from Eightpuzzle import successor_function, goal_test, heuristic
# choice = eval(input("1 for 8 puzzle, stkhra you for the rest: "))
# if choice == 1:
#     import Eightpuzzle

# We should normally/probably take these as input and make them into the format we need
initial_state = np.array([[3, 1, 2],
                       [5, 6, 0],
                       [7, 4, 8]])

goal_state = np.array([[0, 1, 2],
                       [3, 4, 5],
                       [6, 7, 8]])


def uninformed_BFS(state, goal):
    q = Queue()
    nodes = successor_function(state)
    for n in nodes:
        q.put(n)
    while q.empty() == False:
        n = q.get_nowait()
        if(goal_test(n, goal)):
            return n
        nodes = successor_function(n)
        for n in nodes:
            q.put(n)
    return 0

print(uninformed_BFS(initial_state,goal_state))
