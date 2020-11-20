# function names are successor_function, goal_test, and heuristic
from queue import Queue, PriorityQueue
import numpy as np
from Eightpuzzle import successor_function, goal_test, heuristic, pathcost
# choice = eval(input("1 for 8 puzzle, stkhra you for the rest: "))
# if choice == 1:
#     import Eightpuzzle

# We should normally/probably take these as input and make them into the format we need
initial_state = [[1, 4, 2],
                 [3, 7, 5],
                 [6, 8, 0]]

goal_state = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]




def uninformed_BFS(state, goal):
    if(goal_test(state, goal)):
        return state
    q = Queue()
    checked = []
    checked.append(state)
    nodes = successor_function(state)
    for n in nodes:
        q.put(n)
    while q.empty() == False:
        n = q.get_nowait()
        if(goal_test(n, goal)):
            return n
        checked.append(n)
        nodes = successor_function(n)
        flag = False
        for i in nodes:
            flag = False
            for c in checked:
                # comparison = i == c
                # equal = comparison.all()
                if i == c:
                    flag = True
                    break
            if flag == False:
                q.put(i)
            # else:
            #     print('H')
    return 0

def greedyBFS(state, goal):
    if(goal_test(state, goal)):
        return state
    q = PriorityQueue()
    checked = []
    checked.append(state)
    nodes = successor_function(state)
    for n in nodes:
        q.put((heuristic(n, goal), n))
    while q.empty() == False:
        # print(q.queue)
        n = q.get()
        n = n[1]
        # print(n)
        # return
        if(goal_test(n, goal)):
            return n
        checked.append(n)
        nodes = successor_function(n)
        flag = False
        for i in nodes:
            flag = False
            for c in checked:
                if i == c:
                    flag = True
                    break
            if flag == False:
                q.put((heuristic(i,goal), i))
            # else:
                # print("Visited")
    return 0


# print(uninformed_BFS(initial_state, goal_state))
print()
print(greedyBFS(initial_state, goal_state))