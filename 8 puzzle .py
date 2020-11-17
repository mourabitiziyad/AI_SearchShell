import numpy as np

'''
0: blank
N: Tile N

'''

initial_state = np.array([[7, 2, 1],
                          [5, 0, 6],
                          [8, 3, 4]])

goal_state = np.array([[0, 1, 2],
                       [3, 4, 5],
                       [6, 7, 8]])


def goal_test(state, goal_state):
    if np.array_equal(state, goal_state):
        return True
    else:
        return False


def possible_moves(state):
    outcomes = []
    for i in range(3):  # Locating the blank tile
        for j in range(3):
            if state[i][j] == 0:
                brow = i
                bcol = j
    if brow > 0:  # If blank tile can go up
        tempstate = state.copy()
        temp = tempstate[brow][bcol]
        tempstate[brow][bcol] = tempstate[brow-1][bcol]
        tempstate[brow-1][bcol] = temp
        outcomes.append(tempstate)
    if brow < 2:  # If blank tile can go down
        tempstate = state.copy()
        temp = tempstate[brow][bcol]
        tempstate[brow][bcol] = tempstate[brow+1][bcol]
        tempstate[brow+1][bcol] = temp
        outcomes.append(tempstate)
    if bcol > 0:  # If blank tile can go left
        tempstate = state.copy()
        temp = tempstate[brow][bcol]
        tempstate[brow][bcol] = tempstate[brow][bcol-1]
        tempstate[brow][bcol-1] = temp
        outcomes.append(tempstate)
    if bcol < 2:  # If blank tile can go right
        tempstate = state.copy()
        temp = tempstate[brow][bcol]
        tempstate[brow][bcol] = tempstate[brow][bcol+1]
        tempstate[brow][bcol+1] = temp
        outcomes.append(tempstate)
    return outcomes


def heuristic(state, goal):
    # Heuristic chosen is called linear conflicts
    # Manhattan Distance (usedin the overall heuristic)
    MD =0
    for i in range(3):
        for j in range(3):
            #Look up the tile in the goal state
            Gi = 0
            Gj = 0
            for Gi in range(3):
                if state[i][j] in goal[Gi]:
                    for Gj in range(3):
                        if state[i][j] == goal[Gi][Gj]:
                            break
            MD += abs(i - Gi) + abs(j - Gj)
    # Total heuristic is Manhattan Distance plus two times the liner conflicts
    LC = 0
    # We proceed row by row
    for i in range(3):
        conflicted = []
        # We count the number of conflicted tiles in each row
        for j in range(3):
            if state[i][j] in goal[i]:
                conflicted.append(state[i][j])
        # if there is only one conflicting tile, that means no 2 tiles are conflicting
        # in which case we don't do anything.
        if len(conflicted) == 1:
            continue
            # Gi and Si are the indexes of the conflicting tile
            # in the goal state and our state repectively
        if len(conflicted) == 2:
            G1 = np.where(goal[i] == conflicted[0])
            G2 = np.where(goal[i] == conflicted[1])
            S1 = np.where(state[i] == conflicted[0])
            S2 = np.where(state[i] == conflicted[1])
            # We check if the tiles need to be reversed for them to reach their goal
            # that would mean that there is an LC (Linear Conflict)
            if (G1 > G2 and S1 < S2) or (G1 < G2 and S1 > S2):
                LC += 1
        if len(conflicted) == 3:
            G1 = np.where(goal[i] == conflicted[0])
            G2 = np.where(goal[i] == conflicted[1])
            G3 = np.where(goal[i] == conflicted[2])
            S1 = np.where(state[i] == conflicted[0])
            S2 = np.where(state[i] == conflicted[1])
            S3 = np.where(state[i] == conflicted[2])
            # Same logic for three tiles, but we have to test every combination
            if (G1 > G2 and S1 < S2) or (G1 < G2 and S1 > S2):
                LC += 1
            if (G1 > G3 and S1 < S3) or (G1 < G3 and S1 > S3):
                LC += 1
            if (G3 > G2 and S3 < S2) or (G3 < G2 and S3 > S2):
                LC += 1
    # We do the same for columns, by flipping the state and doing it all again
    col1 = [state[0][0], state[1][0], state[2][0]]
    col2 = [state[0][1], state[1][1], state[2][1]]
    col3 = [state[0][2], state[1][2], state[2][2]]
    state = [col1, col2, col3]
    for i in range(3):
        conflicted = []
        for j in range(3):
            if state[i][j] in goal[i]:
                conflicted.append(state[i][j])
        if len(conflicted) == 1:
            continue
        if len(conflicted) == 2:
            G1 = np.where(goal[i] == conflicted[0])
            G2 = np.where(goal[i] == conflicted[1])
            S1 = np.where(state[i] == conflicted[0])
            S2 = np.where(state[i] == conflicted[1])
            # We check if the tiles need to be reversed for them to reach their goal
            # that would mean that there is an LC (Linear Conflict)
            if (G1 > G2 and S1 < S2) or (G1 < G2 and S1 > S2):
                LC += 1
        if len(conflicted) == 3:
            G1 = np.where(goal[i] == conflicted[0])
            G2 = np.where(goal[i] == conflicted[1])
            G3 = np.where(goal[i] == conflicted[2])
            S1 = np.where(state[i] == conflicted[0])
            S2 = np.where(state[i] == conflicted[1])
            S3 = np.where(state[i] == conflicted[2])
            # Same logic for three tiles, but we have to test every combination
            if (G1 > G2 and S1 < S2) or (G1 < G2 and S1 > S2):
                LC += 1
            if (G1 > G3 and S1 < S3) or (G1 < G3 and S1 > S3):
                LC += 1
            if (G3 > G2 and S3 < S2) or (G3 < G2 and S3 > S2):
                LC += 1
    return MD + 2 * LC


# Printing initial node
print("Initial State is: ")
for i in range(3):
    for j in range(3):
        print(initial_state[i][j], end='')
    print()
print()
print()


print(heuristic(initial_state, goal_state))


