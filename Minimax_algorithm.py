
def minimax(board, max_min, AI_letter):
    someone_won = board.check_win()
    if someone_won != 2:
        return someone_won if AI_letter == 'X' else -someone_won

    scores = []
    possible_moves = board.get_possible_moves()

    for move in possible_moves:
        board.make_move(move)
        score = minimax(board, -max_min, AI_letter)
        scores.append(score)
        board.undo_move()

    return min(scores) if max_min == -1 else max(scores)