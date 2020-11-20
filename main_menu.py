import Search_Shell
import MCP
import PegSolitaire
import Eightpuzzle

PegSolitaire_initial_state = [          [2, 2, 0, 0, 0, 2, 2], 
                                        [2, 2, 0, 0, 0, 2, 2],
                                        [0, 0, 0, 0, 0, 0, 0],
                                        [0, 1, 1, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0], 
                                        [2, 2, 0, 0, 0, 2, 2],
                                        [2, 2, 0, 0, 0, 2, 2]   ]
PegSolitaire_goal_state = [         [2, 2, 0, 0, 0, 2, 2], 
                                    [2, 2, 0, 0, 0, 2, 2],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 1, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0], 
                                    [2, 2, 0, 0, 0, 2, 2],
                                    [2, 2, 0, 0, 0, 2, 2]   ]

Eightpuzzle_initial_state = [[1, 4, 2],
                             [3, 7, 5],
                             [6, 8, 0]]
Eightpuzzle_goal_state = [[0, 1, 2],
                          [3, 4, 5],
                          [6, 7, 8]]

MCP_initial_state = [3,3,1,0,0,0]
MCP_goal_state = [0,0,0,3,3,1]

def peg():
    print("\n")
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                           #")
    print("#                                           #")
    print("#       You are now in Peg Solitaire!       #")
    print("#                                           #")
    print("#                                           #")
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                           #")
    print("#                                           #")
    print("#     How would you like to run the game?   #")
    print("#                                           #")
    print("#       1 - Depth-First Search              #")
    print("#       2 - Breadth-First Search            #")
    print("#       3 - Greedy Breadth-First Search     #")
    print("#       4 - A* Search                       #")
    print("#       5 - Go back to Menu                 #")
    print("#                                           #")
    print("#                                           #")
    print("# # # # # # # # # # # # # # # # # # # # # # #")

    choice = (input("\n     Choose:   ") )
    while choice != '1' and choice != '2' and choice != '3' and choice != "4" and choice != "5":
        print("\n     Wrong Value!   ")
        choice = (input("\n     Choose:   "))
    choice = int(choice)
    if choice == 1:
        print("\n     Implementing Depth-First Search...   ")
        print(Search_Shell.uninformed_DFS(PegSolitaire, PegSolitaire_initial_state, PegSolitaire_goal_state).getPath())
        peg()
    elif choice == 2:
        print("\n     Implementing Breadth-First Search...   ")
        print(Search_Shell.uninformed_BFS(PegSolitaire, PegSolitaire_initial_state, PegSolitaire_goal_state).getPath())
        peg()
    elif choice == 3:
        print("\n     Implementing Greedy Breadth-First Search...   ")
        print(Search_Shell.greedyBFS(PegSolitaire, PegSolitaire_initial_state, PegSolitaire_goal_state).getPath())
        peg()
    elif choice == 4:
        print("\n     Implementing A* Search...   ")
        print(Search_Shell.AStar(PegSolitaire, PegSolitaire_initial_state, PegSolitaire_goal_state).getPath())
        peg()
    elif choice == 5:
        main()
    
    return 0

def eight():
    print("\n")
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                           #")
    print("#                                           #")
    print("#         You are now in 8-Puzzle!          #")
    print("#                                           #")
    print("#                                           #")
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                           #")
    print("#                                           #")
    print("#     How would you like to run the game?   #")
    print("#                                           #")
    print("#       1 - Depth-First Search              #")
    print("#       2 - Breadth-First Search            #")
    print("#       3 - Greedy Breadth-First Search     #")
    print("#       4 - A* Search                       #")
    print("#       5 - Go back to Menu                 #")
    print("#                                           #")
    print("#                                           #")
    print("# # # # # # # # # # # # # # # # # # # # # # #")

    choice = (input("\n     Choose:   ") )
    while choice != '1' and choice != '2' and choice != '3' and choice != "4" and choice != "5":
        print("\n     Wrong Value!   ")
        choice = (input("\n     Choose:   "))
    choice = int(choice)
    if choice == 1:
        print("\n     Implementing Depth-First Search...   ")
        eight()
    elif choice == 2:
        print("\n     Implementing Breadth-First Search...   ")
        eight()
    elif choice == 3:
        print("\n     Implementing Greedy Breadth-First Search...   ")
        eight()
    elif choice == 4:
        print("\n     Implementing A* Search...   ")
        eight()
    elif choice == 5:
        main()
    return 0

def cannibals():
    print("\n")
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                           #")
    print("#                                           #")
    print("#              You are now in               #")
    print("#         Missionaries & Cannibals!         #")
    print("#                                           #")
    print("#                                           #")
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                           #")
    print("#                                           #")
    print("#     How would you like to run the game?   #")
    print("#                                           #")
    print("#       1 - Depth-First Search              #")
    print("#       2 - Breadth-First Search            #")
    print("#       3 - Greedy Breadth-First Search     #")
    print("#       4 - A* Search                       #")
    print("#       5 - Go back to Menu                 #")
    print("#                                           #")
    print("#                                           #")
    print("# # # # # # # # # # # # # # # # # # # # # # #")

    choice = (input("\n     Choose:   ") )
    while choice != '1' and choice != '2' and choice != '3' and choice != "4" and choice != "5":
        print("\n     Wrong Value!   ")
        choice = (input("\n     Choose:   "))
    choice = int(choice)
    if choice == 1:
        print("\n     Implementing Depth-First Search...   ")
        print(Search_Shell.uninformed_DFS(MCP, MCP_initial_state, MCP_goal_state).getPath())
        cannibals()
    elif choice == 2:
        print("\n     Implementing Breadth-First Search...   ")
        print(Search_Shell.uninformed_BFS(MCP, MCP_initial_state, MCP_goal_state).getPath())
        cannibals()
    elif choice == 3:
        print("\n     Implementing Greedy Breadth-First Search...   ")
        print(Search_Shell.greedyBFS(MCP, MCP_initial_state, MCP_goal_state).getPath())
        cannibals()
    elif choice == 4:
        print("\n     Implementing A* Search...   ")
        print(Search_Shell.AStar(MCP, MCP_initial_state, MCP_goal_state).getPath())
        cannibals()
    elif choice == 5:
        main()
    return 0

def main():
    print("\n")
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                           #")
    print("#                                           #")
    print("#     Welcome to your very own PieShell!    #")
    print("#                                           #")
    print("#                                           #")
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                           #")
    print("#                                           #")
    print("#     What game would you like to run?      #")
    print("#                                           #")
    print("#        1 - 8-Puzzle                       #")
    print("#        2 - Peg Solitare                   #")
    print("#        3 - Missionaries & Cannibals       #")
    print("#        0 - End Program                    #")
    print("#                                           #")
    print("#                                           #")
    print("# # # # # # # # # # # # # # # # # # # # # # #")

    choice = (input("\n     Choose:   ") )
    while choice != '1' and choice != '2' and choice != '3' and choice != '0':
        print("\n     Wrong Value!   ")
        choice = (input("\n     Choose:   "))
    choice = int(choice)
    if choice == 1:
        eight()
    elif choice == 2:
        peg()
    elif choice == 3:
        cannibals()
    elif choice == 0:
        print("\n     Have a nice day!   ")
        return

main()
