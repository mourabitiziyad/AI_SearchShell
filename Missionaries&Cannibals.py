
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

def goal_test(L, R, LG, RG):
    if L == LG and R == RG:
        return True
    else:
        return False

'''
move1(direction, cannibal/missionary)
move2(direction, cannibal/missionary, cannibal/missionary)

'''
def move1(a,b):
    print("haha")
def move2(a,b,c):
    print("haha")
def successor_function(orig_L, orig_R): # the conditions are coded in a way that does not allow off balance that would result in missionaries being eaten
    outcomes = []
    C, M = 'hello' # ignore
    L, R = orig_L, orig_R
    L_balance = L[0] - L[1]
    R_balance = R[0] - R[1]
    # We keep track of our R_balance and L_balance such that their sum equals 0 
    #all conditions are based on possible states where the missionaries dont get eaten by cannibals
    if L[2] == 1: # boat on the left bank
        if L_balance == 0 and R_balance == 0:
            move2(R, M, C) # L(3,3) and R(0,0) & L(2,2) and R(1,1) & L(1,1) and R(2,2) 
             #append to outcomes 
            if R[1] == 0: # L(3,3) and R(0,0)
                move1(R,C)  #append to outcomes 
                move2(R, C, C)  #append to outcomes 
        elif L_balance == 1 and R_balance == -1:
            move1(R,M) # L(3,2) and R(0,1)
            # L(2,1) and R(1,2) & L(1,0) and R(2,3) not possible
        elif L_balance == 2 and R_balance == -2:
             move2(R, M, M) # L(3,1) and R(0,2)
              # L(2,0) and R(1,3) not possible
        else: #LOL nada 
            pass
    return outcomes

# def successor_function(orig_L, orig_R): # the conditions are coded in a way that does not allow off balance that would result in missionaries being eaten
#     outcomes = []
#     L, R = orig_L, orig_R
#     L_balance = L[0] - L[1]
#     R_balance = R[0] - R[1]
#     if L[2] == 1: # boat on the left bank
#         if L_balance == 0 and L[0]>0: # cannibals and missionaries are equal in numbers and greater than 0
#             # move1(R, C)
#             # add condition to check for number of cannibals on the right
#             move2(R, C, C)
#             move2(R, C, M)
#         elif i == 1:
#             move1(R, M)
#             move2(R, C, M)
#             # add condition to check for number of cannibals on the right
#             move2(R, C, C)
#         elif i == 2: # means that on the left we have 3M 1C, otherwise there would be a lost balance on the right
#             move1(R, C)
#             move2(R, M, M)
#     return outcomes