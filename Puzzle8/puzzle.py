"""
Puzzle8 Game
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
"""

from random import randrange
from functions import *
from SearchAgent import *

def shuffle_puzzle(n):
	puzzle=[0, 1, 2, 3, 4, 5, 6, 7, 8]
	for _ in range(n):
		actions=get_actions(puzzle)
		rand_index=randrange(0,len(actions))
		puzzle=get_state(actions[rand_index],puzzle)
	return puzzle

if __name__ == '__main__':
	# puzzle=shuffle_puzzle(50)
	
	#use the implelemented search strategies (DFS,BFS,UCS) to solve the puzzle
	#print the final solution and the number of expanded nodes for each strategy
	#for DFS use this puzzle [1, 0, 2, 6, 3, 5, 4, 7, 8]

	
	puzzle = [1, 0, 2, 6, 3, 5, 4, 7, 8]
	strategies = ['DFS', 'BFS', 'UCS']
	for strategy in strategies:
		solution = solve(strategy , puzzle)

		if solution:
			print(f"Strategy: {strategy}, {solution}\n")
		else:
			print("Sorry, can't find solution!")
