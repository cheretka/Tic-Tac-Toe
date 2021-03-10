from Board import Board



def move_player(playerLetter, board):
    print('Your turn')
    ok = False
    while not ok:
        print("Which box? : ")
        move = int(input())
        index = [(3 * (move // 10 - 1) + (move % 10)) - 1, playerLetter]
        ok = board.make_move(index)


def move_computer(board, letterAI):
    print('AI turn')
    best_score = -10
    final_move = -1

    possible_moves = board.get_possible_moves()
    for move in possible_moves:
        board.make_move(move)
        score = minimax(board, -1, letterAI)
        board.undo_move()
        if score > best_score:
            best_score = score
            final_move = move

    board.make_move(final_move)


def minimax(board, max_min, letterAI):
    win = board.check_win()
    if win != 2:
        return win if letterAI == 'X' else -win

    scores = []
    possible_moves = board.get_possible_moves()

    for move in possible_moves:
        board.make_move(move)
        score = minimax(board, -max_min, letterAI)
        scores.append(score)
        board.undo_move()

    return min(scores) if max_min == -1 else max(scores)







if __name__ == "__main__":

    print('Welcome to Tic Tac Toe!')
    board = Board()
    board.print()

    human_letter = ''
    while not (human_letter == 'X' or human_letter == 'O'):
        print('Do you want to be X (moves first) or O?')
        human_letter = input().upper()

    AI_letter = 'O' if human_letter == 'X' else 'X'
    current_player = ['X', 'O']


    index = 0
    while True:
        if current_player[index % 2] == human_letter:
            move_player(playerLetter, board)
        else:
            move_computer(board, current_player[index % 2])

        board.print()

        win = board.check_win()
        if (win == -1 and playerLetter == 'O') or (win == 1 and playerLetter == 'X'):
            print('Hooray! You have won the game!')
            break
        elif (win == -1 and AILetter == 'O') or (win == 1 and AILetter == 'X'):
            print('The computer has beaten you! You lose.')
            break
        elif win == 0:
            print('The game is a tie!')
            break

        index += 1

    print('End the game!')