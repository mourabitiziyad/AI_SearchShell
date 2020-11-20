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
        print("DFS")
        peg()
    elif choice == 2:
        print("BFS")
        peg()
    elif choice == 3:
        print("Greedy")
        peg()
    elif choice == 4:
        print("A*")
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
        print("DFS")
        eight()
    elif choice == 2:
        print("BFS")
        eight()
    elif choice == 3:
        print("Greedy")
        eight()
    elif choice == 4:
        print("A*")
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
        print("DFS")
        cannibals()
    elif choice == 2:
        print("BFS")
        cannibals()
    elif choice == 3:
        print("Greedy")
        cannibals()
    elif choice == 4:
        print("A*")
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
