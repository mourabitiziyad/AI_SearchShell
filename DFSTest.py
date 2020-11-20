def uninformed_DFS(state, goal):
    beg = node(state,0)
    if(goal_test(state, goal)):
        return state
    fringe = [] #will be implemented as a stack 
    checked = [] #expanded/closed list 
    nodes = [] #list of successor states

    checked.append(state) 
    """insert is used as a push function. 
    List.insert(i, elem) --> lem is inserted to the list at the ith index. 
    All the elements after elem are shifted to the right.
    """
    nodes = successor_function(state)
    for n in nodes:
        N = node(n, beg)
        fringe.insert(O, N) 
    while fringe.empty() == False:
        N = fringe.pop() #get_nowait() replace if problem 
        if(goal_test(N.puzzle, goal)):
            return N
        checked.append(N.puzzle) #WHAT IS PUZZLE
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
                fringe.insert(O, I) 
            # else:
            #     print('H')
    return beg
