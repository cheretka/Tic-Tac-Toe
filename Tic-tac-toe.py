from Board import *
from Minimax_algorithm import *

# Function that takes a move from the user
def move_player(board, human_letter):
    print('Your turn')
    good_move = False
    while not good_move:
        print("Which box (RowColumn)? : ")
        move = int(input())
        index = [(3 * (move // 10 - 1) + (move % 10)) - 1, human_letter]
        good_move = board.make_move(index)

# Function that selects and takes a step for the bot
def move_computer(board, AI_letter):
    print('AI turn')
    best_score, final_move = -10, -1

    # start Minimax algorithm
    possible_moves = board.get_possible_moves()
    for move in possible_moves:
        board.make_move(move)
        score = minimax(board, -1, AI_letter)
        board.undo_move()
        if score > best_score:
            best_score, final_move = score, move

    board.make_move(final_move)



if __name__ == "__main__":

    print('Welcome to Tic Tac Toe!')
    board = Board()
    board.print()

    # determination for which mark the person and AI will play
    human_letter = ''
    while not (human_letter == 'X' or human_letter == 'O'):
        print('Do you want to be \'X\' (moves first) or \'O\' ?')
        human_letter = input().upper()

    AI_letter = 'O' if human_letter == 'X' else 'X'
    current_player = ['X', 'O']


    # game
    index = 0
    while True:
        # player's move
        if current_player[index % 2] == human_letter:
            move_player(board, human_letter)
        else:
            move_computer(board, current_player[index % 2])

        # show board
        board.print()

        # checking if the game is over
        win = board.check_win()
        if (win == -1 and human_letter == 'O') or (win == 1 and human_letter == 'X'):
            print('Hooray! You have won the game!')
            break
        elif (win == -1 and AI_letter == 'O') or (win == 1 and AI_letter == 'X'):
            print('The computer has beaten you! You lose.')
            break
        elif win == 0:
            print('The game is a tie!')
            break

        index += 1

    print('End the game!')