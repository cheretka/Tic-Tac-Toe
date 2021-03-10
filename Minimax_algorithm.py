# Recursive function that implements the Minimax algorithm
def minimax(board, max_min, AI_letter):
    # if one of the players wins or there are no more empty cells, the function returns a specific value
    someone_won = board.check_win()
    if someone_won != 2:
        return someone_won if AI_letter == 'X' else -someone_won

    # collect in the table scores that we can get when occupying each of the free cells
    scores = []
    possible_moves = board.get_possible_moves()

    for move in possible_moves:
        board.make_move(move)
        score = minimax(board, -max_min, AI_letter)
        scores.append(score)
        board.undo_move()

    # select the cell in which score will be the largest if it's max-algorithm or the smallest in opposite case
    return min(scores) if max_min == -1 else max(scores)