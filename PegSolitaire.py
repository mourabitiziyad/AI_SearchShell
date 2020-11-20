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

class node:
    goal = []
    def __init__(self, state, parent):
        self.puzzle = state
        self.parent = 0
        self.parent = parent

    def setGoal(self,Goal):
        self.goal = Goal

    def getPath(self):
        path = []
        prev = self.parent
        while(prev != 0):
            path.append(prev.puzzle)
            prev = prev.parent
        path.reverse()
        path.append(self.puzzle)
        return path

    def __gt__(self, other):
        return self.puzzle > other.puzzle

def goal_test(state, goal_state): # Make it return a bool to be used in search strategy
    if state == goal_state:
        return True
    else:
        return False

def pathcost(N):
    path = N.getPath()
    return len(path)

def possible_moves_from_index(state, index):
    moves = [] # 2D list to return possible indices to which the peg can move to
    row, column = index[0], index[1]
    try:
        if state[row][column] == 1:
            try: # Try/Catch to avoid out of range errors
                if state[row - 2][column] == 0 and state[row - 1][column] == 1 and row-2 >= 0: # Make sure we don't include a hole with a peg or an "out of bound" (2)
                    moves.append([row-2, column]) # Append the index of the empty hole to the possible moves array
            except IndexError:
                print("errrrrrrrrr")
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
            pass
        else:
            pass
            # print("bruh mark")
    except:
        IndexError
    return moves

def successor_function(state):
    outcomes = []
    visual_rep = []
    backup_state = deepcopy(state)
    for row in range(7):
        for col in range(7):
            moves = possible_moves_from_index(backup_state, [row, col])
            if len(moves) > 0:
                for m in moves:
                    visual_rep.append([[row, col, "==>", m]])
                    backup_state[row][col], backup_state[m[0]][m[1]] = backup_state[m[0]][m[1]], backup_state[row][col]
                    if col == m[1] and row < m[0]:
                        backup_state[row+1][col] = 0
                    elif col == m[1] and row > m[0]:
                        backup_state[row-1][col] = 0
                    elif col < m[1] and row == m[0]:
                        backup_state[row][col+1] = 0
                    elif col > m[1] and row == m[0]:
                        backup_state[row][col-1] = 0
                    visual_rep.append(backup_state)
                    outcomes.append(backup_state)
                    backup_state = deepcopy(state)
    return outcomes

def heuristic(state, goal):  # reaching the goal entails the number of pegs reducing until we reach 1 peg in the middle with no possible moves.
                             # the heuristic will rely on the number of remaining pegs and the possible moves from each one 
    count = 0
    for row in range(7):
        for col in range(7):
            moves = possible_moves_from_index(state, [row, col])
            count += len(moves)
    return count

 