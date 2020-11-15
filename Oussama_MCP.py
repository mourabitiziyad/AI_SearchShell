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

# Goal State
LT = [0,0,0]
RT = [3,3,1]

def goal_test(L, R, LG, RG):
    if L == LG and R == RG:
        return True
    else:
        return False

'''
move1(direction, cannibal/missionary)
move2(direction, cannibal/missionary, cannibal/missionary)
'''

#Ziyad I think we need to pass Li, Ri to have access to them 
def move1(Li,Ri, direction, op):
  if direction=='Right':
    if op == 'cannibals': #move cannibal from left to right
      Ri[1]+=1
      Li[1]-=1
    else: #op == 'missionaries' (move missionary from left to right)
      Ri[0]+=1
      Li[0]-=1
  else: #direction=='Left'
    if op == 'cannibals': #move cannibal from Right to Left 
      Ri[1]-=1
      Li[1]+=1
    else: #op == 'missionaries' (move missionary from right to left)
      Ri[0]-=1
      Li[0]+=1
  

#there's probably a way to write move2 in terms of move1 but fleeeme
def move2 (Li,Ri, direction, op1, op2): 
  if direction=='Right':
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



def successor_function(orig_L, orig_R):
    outcomes = []
    C, M = 'cannibals','missionaries' # ignore
    Li, Ri = orig_L, orig_R
    R,L= 'Right','Left' #Directions 
    L_balance = L[0] - L[1] 
    R_balance = R[0] - R[1]
    #all conditions are based on possible states where the missionaries don't get eaten by cannibals
    #sum of R_balance and L_balance must always equal 0 

    """General Note: after each move function:
    - append to outcomes
    -initialize (Li, Ri = orig_L, orig_R)
    """
    if L[2] == 1: # boat on the left bank
        if L_balance == 0 and R_balance == 0:
            move2(Li, Ri, R, M, C) 
              #L(3,3)/R(0,0) --> L(2,2)/R(1,1)
              #L(2,2)/R(1,1) --> L(1,1)/R(2,2) 
              #L(1,1)/R(2,2) --> L(0,0)/R(3,3) (Goal)
            move2(Li, Ri,R,M,M)
              #L(2,2)/R(1,1) --> L(0,2)/R(3,1) 
            move1(Li, Ri, R,M) #L(1,1)/R(2,2) --> L(0,1)/R(3,2)
            if R[0] == 0: #if no missionaries on right; otherwise game over 
              move1(Li, Ri,R,C) 
                # L(3,3)/R(0,0) --> L(3,2)/R(0,1)
              move2(Li, Ri, R, C, C)
                # L(3,3)/R(0,0) --> L(3,1)/R(0,2)
        elif L_balance == 1 and R_balance == -1:
            move1(Li, Ri, R,M) # L(3,2)/R(0,1) --> L(2,2)/R(1,1)
            if R[0] == 0: #if no missionaries on right; 
              move1(Li, Ri, R,C) # L(3,2)/R(0,1) --> L(3,1)/R(0,2)
              move2(Li, Ri, R, C, C) # L(3,2)/R(0,1) --> L(3,0)/R(0,3)
        elif L_balance == 2 and R_balance == -2:
            move2(Li, Ri, R, M, M) 
              # L(3,1)/ R(0,2) --> L(1,1)/ R(2,2)
              # L(2,0)/R(1,3) game over 
            move1(Li, Ri, R,C) # L(3,1)/R(0,2) --> L(3,0)/R(0,3)
        elif L_balance == 3 and R_balance == -3: 
          move2(Li, Ri, R, C, C) #L(0,3)/R(3,0) --> L(0,1)/R(3,2)
        #L_balance is only negative when the boat is on the left bank, around the last few moves, to transport the cannibals to the right where the 3 missionaries are
        elif L_balance == -1 and R[0] == 3: 
          move1(Li, Ri, R, C) #L(0,1)/R(3,2) --> L(0,0)/R(3,3) (Goal)
        elif L_balance == -2 and R[0] == 3: 
          move1(Li, Ri, R, C) #L(0,2)/R(3,1) --> L(0,1)/R(3,2) 
          move2(Li, Ri, R,C,C) #L(0,2)/R(3,1) --> L(0,0)/R(3,3)
          
    else: #boat on the right bank. Here we focus on the R_balance.
      if R_balance == 0 and L_balance == 0:
        move1(Li, Ri, L, M) #L(2,2)/R(1,1) --> L(3,2)/R(0,1)
        move2(Li, Ri, L,M,C) 
          #L(2,2)/R(1,1) --> L(3,3)/R(0,0)
          #L(1,1)/R(2,2) --> L(2,2)/R(1,1)
        move2(Li, Ri, L,M,M) #L(1,1)/R(2,2) --> L(3,1)/R(0,2)
        #Game over: L(1,1)/R(2,2) --> L(1,2)/R(2,1) or L(2,1)/R(1,2)
        #There's no L(0,0)/R(3,3) --> because goal state 
      elif L_balance == 1 and R_balance == -1:
        move1(Li, Ri, L,C)
          #L(3,2)/R(0,1) --> L(3,3)/R(0,O)
          #Game over: L(3,2)/R(1,2) and L(3,2)/R(2,3)
      elif L_balance == 2 and R_balance == -2: 
        move1(Li, Ri, L,C)
          #L(3,1)/R(0,2) --> L(3,2)/R(0,1)
          #L(0,2)/R(3,1) --> L(0,3)/R(3,0)
        move2(Li, Ri,L,C,C) #L(3,1)/R(0,2) --> L(3,3)/R(0,0)
        move2(Li, Ri, L,M,M) #L(0,2)/R(3,1) --> L(2,2)/R(1,1)
      elif L_balance == 3 and R_balance == -3: 
       move2(Li, Ri, L,C,C) #L(3,0)/R(0,3) -->L(3,2)/R(0,1)
       move1(Li, Ri, L,C)#L(3,0)/R(0,2) --> L(3,1)/R(0,2) 
       #L_balance is negative in the last few moves 
      elif L_balance == -1 and R[0] == 3: 
          move1(Li, Ri, R, C) #L(0,1)/R(3,2) --> L(0,2)/R(3,1) 
    return outcomes

""""
Need to append to outcomes initialize 
and use a test case
Does Ri,Li get updated in function? If so just .append them to outcomes as
If all fails, use just one list (M and C in left with B to suggest if boat/move is left or right)
"""
