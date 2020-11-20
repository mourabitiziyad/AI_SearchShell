# AI_SearchShell

Hamza Ait Hssayne - Oussama Tlaghi - Ziyad Mourabiti
 
Documentation describing exactly how you managed that separation and what the user must do in order to test out your search shell with different puzzles. 

We created a main_menu, in which the user can select the game and the search strategy that they want to be applied. Upon selecting, the solution path is printed for them. The different search strategies in the Search Shell file are given the name of the game and the corresponding initial/goal state. 
For Missionaries and Cannibals, the initial and goal states were clear. For 8-puzzle, we picked an initial state that is good enough to perform a search. For PegSolitaire, we picked a really simple initial state to avoid waiting dozens of minutes depending on the search strategy because of the branching factor.
One can test our code by simply changing the initial states of different games. 
We also added a timeout option that allows the user to input,  in seconds, the maximum time, after which the search terminates. The rationale behind this choice is elaborated on in the next page.
A document that:
Describes, illustrates and discusses your heuristic(s) – there should be just enough description in the code so the programmer can understand how they are computed; 
Discusses how well they and the algorithms worked (or didn’t) in terms of how many nodes were expanded (you may need to refer back to heuristics here); 
Relates any problems you encountered, including not reaching a solution because of space or time complexity; and 
As a group, we started by working on the problem representation individually. When it came time to working on the search shell, we encountered a need to change the problem representation and unife it in some sense:
8-puzzle was coded using numpy arrays. This put us in front of a dilemma of either repeating the puzzle’s code using a regular list, modifying the other games with numpy arrays, or  implementing a conversion in the main_menu or search shell. We decided to go for the safe route (i.e., option 1).
In Missionaries and Cannibals, it was first coded using two lists (L and R). We needed to change the arguments in the successor function and the heuristic, with the new argument being the state. To avoid repeating the code from scratch, inside the functions, we divide up the state into the two lists. 
Perhaps, the most important unification is when we created a node class. The class allowed us to generalize the code through the attributes (i.e., puzzle and parent) and the functions (i.e., setGoal and getPath)
When it comes to the interface (main_menu), we were very relieved when passing the game name as a parameter to the search shell worked. That allowed us to truly make the shell problem-independent.
The heuristics were discussed in each game representation as comments. 
With regards to algorithms and problems encountered, as we have mentioned above, we picked relatively easy initial states for 8-puzzle and Pegsolitaire for many reasons related to the game itself and memory and time limitations because of the frontier/fringe. 
For 8-puzzle, the number of node expansions and the size of the frontier can greatly vary because depending on the initial set, we can only reach a specific portion of the state space (i.e., there’s a possibility the search won’t find the goal state). 
In general, Pegsolitaire results in a big branching factor because of the possible moves from each 1. In certain search strategies, namely BFS, the size of the frontier can become an issue with regards to space complexity. In all search strategies, it can take up to dozens of minutes to find the goal state. 
We set a timeout function in order to regulate the time complexity issue. The timeout function allows the user to input,  in seconds, the maximum time, after which the search terminates.
Some interesting observation we had while testing the timeout
With timeout set for 0.1 seconds, the only search strategy that worked within this limit in the Missionaries and Cannibals game is A*.
With timeout set for 0.001 seconds, the only search strategy that worked within this limit in the PegSolitaire initial state that we had was Depth First Search.
