from copy import copy, deepcopy
'''
L: Left Bank
R: Right Bank
M: Number of Missionaries [0, 3]
C: Number of Cannibals [0, 3]
B: 1 if Boat is on that bank, 0 otherwise
'''
# Initial State
# [M, C, B]
L0 = [3,3,1] 
R0 = [0,0,0]

# Goal State
LG = [0,0,0]
RG = [3,3,1]

# Test State
RT = [2,2,1]
LT = [1,1,0]

def goal_test(L, R, LG, RG):
    if L == LG and R == RG:
        return True
    else:
        return False

def step_cost():
    return 1

'''
move1(direction, cannibal/missionary)
move2(direction, cannibal/missionary, cannibal/missionary)
'''

#Ziyad I think we need to pass Li, Ri to have access to them 
def move1(Li,Ri, direction, op):
  if direction=='Right':
    Li[2] = 0
    Ri[2] = 1
    if op == 'cannibals': #move cannibal from left to right
      Ri[1]+=1
      Li[1]-=1
    else: #op == 'missionaries' (move missionary from left to right)
      Ri[0]+=1
      Li[0]-=1
  else: #direction=='Left'
    Li[2] = 1
    Ri[2] = 0
    if op == 'cannibals': #move cannibal from Right to Left 
      Ri[1]-=1
      Li[1]+=1
    else: #op == 'missionaries' (move missionary from right to left)
      Ri[0]-=1
      Li[0]+=1
  return Li, Ri
  

#there's probably a way to write move2 in terms of move1 but fleeeme
def move2 (Li,Ri, direction, op1, op2): 
  if direction=='Right':
    Li[2] = 0
    Ri[2] = 1
    if op1 == 'cannibals': #move cannibal from left to right
      Ri[1]+=1
      Li[1]-=1
    else: #op1 == 'missionaries' (move missionary from left to right)
      Ri[0]+=1
      Li[0]-=1
    if op2 == 'cannibals': 
      Ri[1]+=1
      Li[1]-=1
    else: #op2 == 'missionaries' 
      Ri[0]+=1
      Li[0]-=1
  else: #direction=='Left'
    Li[2] = 1
    Ri[2] = 0
    if op1 == 'cannibals': #move cannibal from Right to Left 
      Ri[1]-=1
      Li[1]+=1
    else: #op1 == 'missionaries' (move missionary from right to left)
      Ri[0]-=1
      Li[0]+=1
    if op2 == 'cannibals': 
      Ri[1]-=1
      Li[1]+=1
    else: #op2 == 'missionaries' 
      Ri[0]-=1
      Li[0]+=1
  return Li, Ri
"""
When using successor function in search shell, need to have a condition if goal_test is true quit.
We assume that the successor function does not expand the goal_node.

"""
def successor_function(orig_L, orig_R):
    L_outcomes, R_outcomes = [], []
    C, M = 'cannibals','missionaries' # ignore
    Li = deepcopy(orig_L)
    Ri = deepcopy(orig_R)
    Right,Left= 'Right','Left' #Directions 
    L_balance = Li[0] - Li[1] 
    R_balance = Ri[0] - Ri[1]
    #all conditions are based on possible states where the missionaries don't get eaten by cannibals
    #sum of R_balance and L_balance must always equal 0 
    if Li[2] == 1: # boat on the left bank
      if L_balance == 0 and R_balance == 0:
        Li, Ri = move2(Li, Ri, Right, M, C)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
          #L(3,3)/R(0,0) --> L(2,2)/R(1,1)
          #L(2,2)/R(1,1) --> L(1,1)/R(2,2) 
          #L(1,1)/R(2,2) --> L(0,0)/R(3,3) (Goal)
        if (Li[0] - 2 > 0 and Li[0] - 2 >=Li[1]) or Li[0] - 2 == 0 :
          Li, Ri = move2(Li, Ri,Right,M,M)
          L_outcomes.append(Li)
          R_outcomes.append(Ri)
          Li = deepcopy(orig_L)
          Ri = deepcopy(orig_R)
          #L(2,2)/R(1,1) --> L(0,2)/R(3,1) 
        if (Li[0] - 1 > 0 and Li[0] - 1 >= Li[1]) or Li[0] - 1 == 0:
          Li, Ri = move1(Li, Ri, Right,M) #L(1,1)/R(2,2) --> L(0,1)/R(3,2)
          L_outcomes.append(Li)
          R_outcomes.append(Ri)
          Li = deepcopy(orig_L)
          Ri = deepcopy(orig_R)
        if Ri[0] == 0: #if no missionaries on right; otherwise game over 
          Li, Ri = move1(Li, Ri,Right,C)
          L_outcomes.append(Li)
          R_outcomes.append(Ri)
          Li = deepcopy(orig_L)
          Ri = deepcopy(orig_R)
            # L(3,3)/R(0,0) --> L(3,2)/R(0,1)
          Li, Ri = move2(Li, Ri, Right, C, C)
          L_outcomes.append(Li)
          R_outcomes.append(Ri)
          Li = deepcopy(orig_L)
          Ri = deepcopy(orig_R)
            # L(3,3)/R(0,0) --> L(3,1)/R(0,2)
      elif L_balance == 1 and R_balance == -1:
        Li, Ri = move1(Li, Ri, Right,M) # L(3,2)/R(0,1) --> L(2,2)/R(1,1)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
        if Ri[0] == 0: #if no missionaries on right; 
          Li, Ri = move1(Li, Ri, Right,C) # L(3,2)/R(0,1) --> L(3,1)/R(0,2)
          L_outcomes.append(Li)
          R_outcomes.append(Ri)
          Li = deepcopy(orig_L)
          Ri = deepcopy(orig_R)
          Li, Ri = move2(Li, Ri, Right, C, C) # L(3,2)/R(0,1) --> L(3,0)/R(0,3)
          L_outcomes.append(Li)
          R_outcomes.append(Ri)
          Li = deepcopy(orig_L)
          Ri = deepcopy(orig_R)
      elif L_balance == 2 and R_balance == -2:
        Li, Ri = move2(Li, Ri, Right, M, M) 
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
          # L(3,1)/ R(0,2) --> L(1,1)/ R(2,2)
          # L(2,0)/R(1,3) game over 
        Li, Ri = move1(Li, Ri, Right,C) # L(3,1)/R(0,2) --> L(3,0)/R(0,3)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
      # elif L_balance == 3 and R_balance == -3: 
      #   Li, Ri = move2(Li, Ri, Left, C, C) #L(3,0)/R(0,3) --> L(3,2)/R(0,1)
      #   L_outcomes.append(Li)
      #   R_outcomes.append(Ri)
      #   Li = deepcopy(orig_L)
      #   Ri = deepcopy(orig_R)
      #L_balance is only negative around the last few moves, to transport the cannibals to the right where the 3 missionaries are
      elif L_balance == -1 and Ri[0] == 3: 
        Li, Ri = move1(Li, Ri, Right, C) #L(0,1)/R(3,2) --> L(0,0)/R(3,3) (Goal)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
      elif (L_balance == -2 or L_balance == -3) and Ri[0] == 3: 
        Li, Ri = move1(Li, Ri, Right, C) #L(0,2)/R(3,1) --> L(0,1)/R(3,2) 
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
        Li, Ri = move2(Li, Ri, Right,C,C) #L(0,2)/R(3,1) --> L(0,0)/R(3,3)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
          
    else: #boat on the right bank. Here we focus on the R_balance.
      if R_balance == 0 and L_balance == 0:
        if(Ri[0] - 1 > 0 and Ri[0] - 1 >= Ri[1]) or Ri[0] - 1 == 0:
          Li, Ri = move1(Li, Ri, Left, M) #L(2,2)/R(1,1) --> L(3,2)/R(0,1)
          L_outcomes.append(Li)
          R_outcomes.append(Ri)
          Li = deepcopy(orig_L)
          Ri = deepcopy(orig_R)
        Li, Ri = move2(Li, Ri, Left,M,C) 
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
          #L(2,2)/R(1,1) --> L(3,3)/R(0,0)
          #L(1,1)/R(2,2) --> L(2,2)/R(1,1)
        if (Ri[0] - 2 > 0 and Ri[0] - 2 >=Ri[1]) or Ri[0] - 2 == 0:
          Li, Ri = move2(Li, Ri, Left,M,M) #L(1,1)/R(2,2) --> L(3,1)/R(0,2)
          L_outcomes.append(Li)
          R_outcomes.append(Ri)
          Li = deepcopy(orig_L)
          Ri = deepcopy(orig_R)
        #Game over: L(1,1)/R(2,2) --> L(1,2)/R(2,1) or L(2,1)/R(1,2)
        #There's no L(0,0)/R(3,3) --> because goal state
      elif L_balance == 1 and R_balance == -1:
        Li, Ri = move1(Li, Ri, Left,C)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
          #L(3,2)/R(0,1) --> L(3,3)/R(0,O)
          #Game over: L(3,2)/R(1,2) and L(3,2)/R(2,3)
      elif L_balance == 2 and R_balance == -2: 
        Li, Ri = move1(Li, Ri, Left,C)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
          #L(3,1)/R(0,2) --> L(3,2)/R(0,1)
        Li, Ri = move2(Li, Ri,Left,C,C) #L(3,1)/R(0,2) --> L(3,3)/R(0,0)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
 
      elif L_balance == 3 and R_balance == -3: 
        Li, Ri = move2(Li, Ri, Left,C,C) #L(3,0)/R(0,3) -->L(3,2)/R(0,1)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
        Li, Ri = move1(Li, Ri, Left,C)#L(3,0)/R(0,2) --> L(3,1)/R(0,2) 
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
        #L_balance is negative in the last few moves 
      elif L_balance == -1 and Ri[0] == 3: 
        Li, Ri = move1(Li, Ri, Left, C) #L(0,1)/R(3,2) --> L(0,2)/R(3,1) 
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
        Li, Ri = move2(Li, Ri, Left,C,C)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
        Li, Ri = move1(Li, Ri, Left, M) #L(2,2)/R(1,1) --> L(3,2)/R(0,1)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
      elif L_balance == -2 and R_balance == 2:
        Li, Ri = move2(Li, Ri, Left,M,M) #L(0,2)/R(3,1) --> L(2,2)/R(1,1)
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
        Li, Ri = move1(Li, Ri, Left, C) 
        L_outcomes.append(Li)
        R_outcomes.append(Ri)
        Li = deepcopy(orig_L)
        Ri = deepcopy(orig_R)
    return L_outcomes, R_outcomes

def heuristic_function(Li):
  return (Li[0] + Li[1])

'''
For the heuristic, we will compare on the basis of the left bank (since the goal state is LG=0,0,0) 
so the best node from the ones generated by the successor function is intuitively the one where the number of Missionaries and Cannibals 
is less (on the left bank). Since the heuristic function needs to be admissible 
(i.e., underestimates the actual distance from goal) for the informed search to return an optimal solution, 
we will produce the heuristic on a relaxed version of the problem. 
The relaxation we choose is if the cannibals didn't eat the missionaries, meaning we can freely send the cannibals/missionaries to the right bank. 
In this scenario, the number of people in the left bank (in this relaxed problem) will be less than the usual problem. 
'''

LT = [3,3,1]
RT = [0,0,0]

L_out, R_out = successor_function(LT, RT)
for i in range(len(L_out)):
  print("From, ", LT, RT, "to", L_out[i], " and", R_out[i])
