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
print("#                                           #")
print("#                                           #")
print("# # # # # # # # # # # # # # # # # # # # # # #")

choice = (input("\n     Choose:   ") )
while choice != '1' and choice != '2' and choice != '3':
    print("\n     Wrong Value!   ")
    choice = (input("\n     Choose:   "))
