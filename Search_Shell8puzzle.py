# function names are successor_function, goal_test, and heuristic
from queue import Queue, PriorityQueue
import numpy as np
from Eightpuzzle import successor_function, goal_test, heuristic, pathcost, node
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

G = node(goal_state, 0)
G.setGoal(goal_state)


def uninformed_BFS(state, goal):
    beg = node(state,0)
    if(goal_test(state, goal)):
        return state
    q = Queue()
    checked = []
    checked.append(state)
    nodes = successor_function(state)
    for n in nodes:
        N = node(n, beg)
        q.put(N)
    while q.empty() == False:
        N = q.get_nowait()
        if(goal_test(N.puzzle, goal)):
            return N
        checked.append(N.puzzle)
        nodes = successor_function(N.puzzle)
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
                I = node(i,N)
                q.put(I)
            # else:
            #     print('H')
    return beg

def greedyBFS(state, goal):
    beg = node(state,0)
    if(goal_test(state, goal)):
        return state
    q = PriorityQueue()
    checked = []
    checked.append(state)
    nodes = successor_function(state)
    for n in nodes:
        N = node(n, beg)
        q.put((heuristic(n, goal), N))
    while q.empty() == False:
        N = q.get()
        N = N[1]
        # print(n)
        # return
        if(goal_test(N.puzzle, goal)):
            return N
        checked.append(N.puzzle)
        nodes = successor_function(N.puzzle)
        flag = False
        for i in nodes:
            flag = False
            for c in checked:
                if i == c:
                    flag = True
                    break
            if flag == False:
                I = node(i,N)
                q.put((heuristic(i,goal), I))
            
    return 0

def AStar(state, goal):
    beg = node(state,0)
    if(goal_test(state, goal)):
        return state
    q = PriorityQueue()
    checked = []
    checked.append(state)
    nodes = successor_function(state)
    for n in nodes:
        N = node(n, beg)
        q.put((heuristic(n, goal) + pathcost(N), N))
    while q.empty() == False:
        N = q.get()
        N = N[1]
        # print(n)
        # return
        if(goal_test(N.puzzle, goal)):
            return N
        checked.append(N.puzzle)
        nodes = successor_function(N.puzzle)
        flag = False
        for i in nodes:
            flag = False
            for c in checked:
                if i == c:
                    flag = True
                    break
            if flag == False:
                I = node(i,N)
                q.put((heuristic(i,goal) + pathcost(I), I))
            
    return 0

# print(uninformed_BFS(initial_state, goal_state))
print()
print(greedyBFS(initial_state, goal_state).getPath())
print()
print()
print(AStar(initial_state, goal_state).getPath() )