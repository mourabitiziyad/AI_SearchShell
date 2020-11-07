import numpy as np

'''
0: blank
N: Tile N

'''

initial_state = np.array( [   			[7, 2, 4], 
										[5, 0, 6],
										[8, 3, 1]     ])

goal_state = np.array([      	[0, 1, 2], 
                    			[3, 4, 5],
                    			[6, 7, 8]     ])

def goal_test(state, goal_state):
    if np.array_equal(state, goal_state):
        print("Al hamdulillah!")
    else:
        print("Tchfo")

def possible_moves(state):
		outcomes = []
		for i in range (3): #Locating the blank tile
			for j in range (3):
				if state[i][j] == 0 :
					brow = i
					bcol = j
		if brow > 0: #If blank tile can go up
			tempstate = state.copy()
			temp = tempstate[brow][bcol]
			tempstate[brow][bcol] = tempstate[brow-1][bcol]
			tempstate[brow-1][bcol] = temp
			outcomes.append(tempstate)
		if brow < 2: #If blank tile can go down
			tempstate = state.copy()
			temp = tempstate[brow][bcol]
			tempstate[brow][bcol] = tempstate[brow+1][bcol]
			tempstate[brow+1][bcol] = temp
			outcomes.append(tempstate)
		if bcol > 0: #If blank tile can go left
			tempstate = state.copy()
			temp = tempstate[brow][bcol]
			tempstate[brow][bcol] = tempstate[brow][bcol-1]
			tempstate[brow][bcol-1] = temp
			outcomes.append(tempstate)
		if bcol < 2: #If blank tile can go right
			tempstate = state.copy()
			temp = tempstate[brow][bcol]
			tempstate[brow][bcol] = tempstate[brow][bcol+1]
			tempstate[brow][bcol+1] = temp
			outcomes.append(tempstate)
		return outcomes
    


#Printing initial node
print("Initial State is: ")                
for i in range (3):
	for j in range(3):
		print(initial_state[i][j], end = '')
	print()
print()
print()

#Printing children nodes
print("Children nodes are: ")

nodes = possible_moves(initial_state)
for node in (nodes):
	for i in range (3):
		for j in range(3):
			print(node[i][j], end = '')
		print()
	print()
	print()

#Checking if any of the children is the goal
#This basically checks if goal is one move away
for node in (nodes):
	goal_test(node, goal_state)		
