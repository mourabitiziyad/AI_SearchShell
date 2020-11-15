from copy import copy, deepcopy
'''
0: hole with no peg
1: hole with a peg
2: out of bound (the board is cross-shaped)

'''

test_state = [          [2, 2, 0, 1, 1, 2, 2], 
                        [2, 2, 1, 1, 0, 2, 2],
                        [1, 1, 0, 1, 0, 1, 1],
                        [1, 0, 0, 0, 0, 1, 1],
                        [0, 1, 0, 1, 0, 0, 1],
                        [2, 2, 0, 0, 0, 2, 2], 
                        [2, 2, 0, 0, 0, 2, 2]   ]

initial_state = [       [2, 2, 1, 1, 1, 2, 2], 
                        [2, 2, 1, 1, 1, 2, 2],
                        [1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 0, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1],
                        [2, 2, 1, 1, 1, 2, 2], 
                        [2, 2, 1, 1, 1, 2, 2]   ]

goal_state = [          [2, 2, 0, 0, 0, 2, 2], 
                        [2, 2, 0, 0, 0, 2, 2],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0], 
                        [2, 2, 0, 0, 0, 2, 2],
                        [2, 2, 0, 0, 0, 2, 2]   ]



def show_state(state):
    # file1 = open('possible_moves.txt', 'a') 
    # for i in state:
    #     file1.writelines(str(i))
    #     file1.write("\n")
    for i in state:
        print(i)
    print('\n')
    # file1.write("\n")

def goal_test(state, goal_state): # Make it return a bool to be used in search strategy
    if state == goal_state:
        print("hallelujah!")
    else:
        print("oh no")

def step_cost():
    return 1

def possible_moves_from_index(state, index):
    moves = [] # 2D list to return possible indices to which the peg can move to
    row, column = index[0], index[1]
    if state[row][column] == 1:
        try: # Try/Catch to avoid out of range errors
            if state[row - 2][column] == 0 and state[row - 1][column] == 1 and row-2 >= 0: # Make sure we don't include a hole with a peg or an "out of bound" (2)
                moves.append([row-2, column]) # Append the index of the empty hole to the possible moves array
        except IndexError:
            pass
        
        try:
            if state[row + 2][column] == 0 and state[row + 1][column] == 1:
                moves.append([row+2, column])
        except IndexError:
            pass
        
        try:
            if state[row][column - 2] == 0 and state[row][column - 1] == 1 and column - 2 >= 0:
                moves.append([row, column - 2])
        except IndexError:
            pass
        
        try:
            if state[row][column + 2] == 0 and state[row][column + 1] == 1:
                moves.append([row, column + 2])
        except IndexError:
            pass
        
    elif state[row][column] == 0:
        # print("something is wrong with the fringe")
        pass
    else:
        pass
        # print("bruh mark")
    return moves

# def all_possible_moves(state):
#     # all_moves = []
#     for row in range(7):
#         for col in range(7):
#             moves = possible_moves_from_index(state, [row, col])
#             if len(moves) > 0: # to be added before using possible_moves_from_index IN SEARCH STRATEGY
#                 print(row, ",", col, ":", moves) # to be replaced by return (action, state) because successor function

def all_possible_moves(state):
    # all_moves = []
    for row in range(7):
        for col in range(7):
            moves = possible_moves_from_index(state, [row, col])
            if len(moves) > 0: # to be added before using possible_moves_from_index IN SEARCH STRATEGY
                print(row, ",", col, ":", moves) # to be replaced by return (action, state) because successor function

def successor_function(state):
    outcomes = []
    backup_state = deepcopy(state)
    for row in range(7):
        for col in range(7):
            moves = possible_moves_from_index(backup_state, [row, col])
            if len(moves) > 0:
                print(row, col, moves)
                for m in moves:
                    backup_state[row][col], backup_state[m[0]][m[1]] = backup_state[m[0]][m[1]], backup_state[row][col]
                    if col == m[1] and row < m[0]:
                        backup_state[row+1][col] = 0
                    elif col == m[1] and row > m[0]:
                        backup_state[row-1][col] = 0
                    elif col < m[1] and row == m[0]:
                        backup_state[row][col+1] = 0
                    elif col > m[1] and row == m[0]:
                        backup_state[row][col-1] = 0
                    outcomes.append(backup_state)
                    backup_state = deepcopy(state)
    return outcomes

def heuristic_function(state):  # reaching the goal entails the number of pegs reducing until we reach 1 peg in the middle with no possible moves.
                                # the heuristic will rely on the number of remaining pegs and the possible moves from each one 
    count = 0
    for row in range(7):
        for col in range(7):
            moves = possible_moves_from_index(state, [row, col])
            count += len(moves)
    return count
    
out = successor_function(test_state)
count = heuristic_function(test_state)
print("the count is: ", count)
for i in test_state:
    print (i)
print("\n##################\n")
for i in out:
    for f in i:
        print (f)
    print("\n")
 