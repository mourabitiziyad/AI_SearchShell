# function names are successor_function, goal_test, and heuristic
from queue import Queue, PriorityQueue
import time
import Eightpuzzle
import MCP
import PegSolitaire

def uninformed_DFS(game, state, goal, timeout):
    start_time = time.time()
    G = game.node(goal, 0)
    G.setGoal(goal)
    beg = game.node(state,0)
    if(game.goal_test(state, goal)):
        reportPath(beg)
        return beg
    fringe = [] # implemented as a stack 
    checked = [] # expanded/closed list 
    nodes = [] # list of successor states

    checked.append(state) 
    """
    insert is used as a push function. 
    List.insert(i, elem) --> lem is inserted to the list at the ith index. 
    All the elements after elem are shifted to the right.
    """
    nodes = game.successor_function(state)
    for n in nodes:
        N = game.node(n, beg)
        fringe.insert(0, N) 
    while len(fringe) != 0:
        N = fringe.pop() 
        if(game.goal_test(N.puzzle, goal)):
            reportPath(N)
            checked.append(N.puzzle)
            reportExpanded(checked)
            return N
        checked.append(N.puzzle) 
        nodes = game.successor_function(N.puzzle)
        flag = False
        for i in nodes:
            flag = False
            for c in checked:
                if time.time() - start_time > timeout:
                    return 404
                if i == c:
                    flag = True
                    break
            if flag == False:
                I = game.node(i,N)
                fringe.insert(0, I) 
    return beg


def uninformed_BFS(game, state, goal, timeout):
    start_time = time.time()
    G = game.node(goal, 0)
    G.setGoal(goal)
    beg = game.node(state,0)
    if(game.goal_test(state, goal)):
        reportPath(beg)
        return beg
    q = Queue() # This is the fringe
    checked = [] # This is the closed list
    checked.append(state)
    nodes = game.successor_function(state)
    for n in nodes:
        N = game.node(n, beg)
        q.put(N)
    while q.empty() == False:
        N = q.get_nowait()
        if(game.goal_test(N.puzzle, goal)):
            reportPath(N)
            checked.append(N.puzzle)
            reportExpanded(checked)
            return N
        checked.append(N.puzzle)
        nodes = game.successor_function(N.puzzle)
        flag = False
        for i in nodes:
            flag = False
            for c in checked:
                if time.time() - start_time > timeout:
                    return 404
                if i == c:
                    flag = True
                    break
            if flag == False:
                I = game.node(i,N)
                q.put(I)
    return 0

def greedyBFS(game, state, goal, timeout):
    start_time = time.time()
    G = game.node(goal, 0)
    G.setGoal(goal)
    beg = game.node(state,0)
    if(game.goal_test(state, goal)):
        reportPath(beg)
        return beg
    q = PriorityQueue() # This is the fringe
    checked = [] # This is the closed list
    checked.append(state)
    nodes = game.successor_function(state)
    for n in nodes:
        N = game.node(n, beg)
        q.put((game.heuristic(n, goal), N))
    while q.empty() == False:
        N = q.get()
        N = N[1]
        if(game.goal_test(N.puzzle, goal)):
            reportPath(N)
            checked.append(N.puzzle)
            reportExpanded(checked)
            return N
        checked.append(N.puzzle)
        nodes = game.successor_function(N.puzzle)
        flag = False
        for i in nodes:
            flag = False
            for c in checked:
                if time.time() - start_time > timeout:
                    return 404
                if i == c:
                    flag = True
                    break
            if flag == False:
                I = game.node(i,N)
                q.put((game.heuristic(i,goal), I))
            
    return 0

def AStar(game, state, goal, timeout):
    start_time = time.time()
    G = game.node(goal, 0)
    G.setGoal(goal)
    beg = game.node(state,0)
    if(game.goal_test(state, goal)):
        reportPath(beg)
        return beg
    q = PriorityQueue() # this is the frontier
    checked = [] # this is the closed list
    checked.append(state)
    nodes = game.successor_function(state)
    for n in nodes:
        N = game.node(n, beg)
        q.put((game.heuristic(n, goal) + game.pathcost(N), N))
    while q.empty() == False:
        N = q.get()
        N = N[1]
        if(game.goal_test(N.puzzle, goal)):
            reportPath(N)
            checked.append(N.puzzle)
            reportExpanded(checked)
            return N
        checked.append(N.puzzle)
        nodes = game.successor_function(N.puzzle)
        flag = False
        for i in nodes:
            flag = False
            for c in checked:
                if time.time() - start_time > timeout:
                    return 404
                if i == c:
                    flag = True
                    break
            if flag == False:
                I = game.node(i,N)
                q.put((game.heuristic(i,goal) + game.pathcost(I), I))
            
    return 0

def reportPath(N):

    print("The path taken was: ")
    path = N.getPath()
    for n in path:
        print(n)
        print()

def reportExpanded(expanded):
    print("The number of nodes expanded is : %d" % len(expanded))
    print()
    print("The nodes expanded are: ")
    for n in expanded:
        print(n)
        print()