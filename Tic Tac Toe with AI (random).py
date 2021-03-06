import random


class Board:
    def __init__(self):
        self.values = [' ' for x in range(9)]
        self.player_pos = {'X': [], 'O': []}

    def print(self):
        print("\n")
        print("\t      1      2     3")
        print("\t          |     |")
        print("\t 1     {}  |  {}  |  {}".format(self.values[0], self.values[1], self.values[2]))
        print('	    ______|_____|_____')
        print("\t          |     |")
        print("\t 2     {}  |  {}  |  {}".format(self.values[3], self.values[4], self.values[5]))
        print('	    ______|_____|_____')
        print("\t          |     |")
        print("\t 3     {}  |  {}  |  {}".format(self.values[6], self.values[7], self.values[8]))
        print("\t          |     |")
        print("\n")

    def get_board(self):
        return self.values

    def check_win(self, cur_player):
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        for x in soln:
            if all(y in self.player_pos[cur_player] for y in x):
                return True

        return False

    def set_value(self, player, position):
        if self.values[position - 1] == ' ':
            self.values[position - 1] = player
            self.player_pos[player].append(position)
            return True

        return False


def input_player():
    letter = ''

    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    return letter


def move_player(playerLetter, board):
    ok = False
    while ok == False:
        print("Which box? : ")
        move = int(input())
        ok = board.set_value(playerLetter, (3 * (move // 10 - 1) + (move % 10)))


def move_computer(letter, board):
    possibleMoves = []
    for x in range(9):
        if board.values[x] == ' ':
            possibleMoves.append(x)

    ok = board.set_value(letter, random.choice(possibleMoves) + 1)


if __name__ == "__main__":

    print('Welcome to Tic Tac Toe!')

    values1 = [' ' for x in range(9)]

    board = Board()
    board.print()

    playerLetter = input_player()
    cur_player = ['X', 'O']

    for x in range(9):

        if cur_player[x % 2] == playerLetter:
            move_player(playerLetter, board)
        else:
            move_computer(cur_player[x % 2], board)

        board.print()
        if board.check_win(cur_player[x % 2]):
            if cur_player[x % 2] == playerLetter:
                print('Hooray! You have won the game!')
                raise SystemExit(0)
            else:
                print('The computer has beaten you! You lose.')
                raise SystemExit(0)

    print('The game is a tie!')
