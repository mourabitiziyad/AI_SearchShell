'''
0: hole with no peg
1: hole with a peg
2: out of bound (the board is cross-shaped)

'''

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

def goal_test(state, goal_state):
    if state == goal_state:
        print("hallelujah!")
    else:
        print("oh no")

def possible_moves_from_index(state, index):
    moves = [] # 2D list to return possible indices to which the peg can move to
    row, column = index[0], index[1]
    if state[row][column] == 1:
        try: # Try/Catch to avoid out of range errors
            if state[row - 2][column] == 0: # Make sure we don't include a hole with a peg or an "out of bound" (2)
                moves.append([row-2, column]) # Append the index of the empty hole to the possible moves array
        except IndexError:
            pass
        
        try:
            if state[row + 2][column] == 0:
                moves.append([row+2, column])
        except IndexError:
            pass
        
        try:
            if state[row][column - 2] == 0:
                moves.append([row, column - 2])
        except IndexError:
            pass
        
        try:
            if state[row][column + 2] == 0:
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

def all_possible_moves(state):
    # all_moves = []
    for row in range(7):
        for col in range(7):
            moves = possible_moves_from_index(state, [row, col])
            if len(moves) > 0: 
                print(row, ",", col, ":", moves)

                



# goal_test(initial_state, goal_state)
# moves = possible_moves_from_index(initial_state, [3,1])
# print(moves)

all_possible_moves(goal_state)
