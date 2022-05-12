def puzzle_currentState(puzzle):
    i = puzzle_cheak(puzzle)

    available_moves = []
    if i in [1, 2, 4, 5, 7, 8]:
        available_moves.append('<')

    if i in [0, 1, 3, 4, 6, 7]:
        available_moves.append('>')

    if i in [3, 4, 5, 6, 7, 8]:
        available_moves.append('^')

    if i in [0, 1, 2, 3, 4, 5]:
        available_moves.append('v')

    return available_moves


def puzzle_userAction(puzzle, selected_move):
    i = puzzle_cheak(puzzle)
    
    if selected_move == '>':
        puzzle[i], puzzle[i+1] = puzzle[i+1], puzzle[i]
    if selected_move == '<':
        puzzle[i], puzzle[i-1] = puzzle[i-1], puzzle[i]
    if selected_move == '^':
        puzzle[i], puzzle[i-3] = puzzle[i-3], puzzle[i]
    if selected_move == 'v':
        puzzle[i], puzzle[i+3] = puzzle[i+3], puzzle[i]
    return puzzle

def puzzle_cheak(puzzle):
    for i in range(len(puzzle)):
        if puzzle[i] == 0: break
        else: continue
    return i


def puzzle_goal(puzzle):
    win = [
        0, 1, 2,
        3, 4, 5,
        6, 7, 8
    ]
    if puzzle == win:
        return True
    else:
        return False