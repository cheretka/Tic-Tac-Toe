class Board:
    def __init__(self):
        self.values = [' ' for x in range(9)]

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


    def check_win(self, cur_player):
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        for x in soln:
            counter = 0
            for ind in x:
                if self.values[ind - 1] == cur_player:
                    counter += 1
            if counter == 3:

                return True

        return False


    def is_full(self):
        for y in self.values:
            if y == " ":
                return False

        return True





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
        # ok = board.set_value(playerLetter, (3 * (move // 10 - 1) + (move % 10)))
        index = (3 * (move // 10 - 1) + (move % 10)) -1
        if board.values[index] == ' ':
            board.values[index] = playerLetter
            ok=True


def move_computer(board, letterAI, letterH):
    bestScore = -10
    move = -1
    for x in range(9):
        if board.values[x] == ' ':

            board.values[x] = letterAI
            score = minimax(board, "min", letterAI, letterH)
            board.values[x] = ' '

            if score>bestScore:
                bestScore = score
                move = x

    board.values[move] = letterAI



def minimax(board, max_min, letterAI, letterH):
    if board.check_win(letterAI):
        return 1
    if board.check_win(letterH):
        return -1
    if board.is_full():
        return 0

    if max_min == "max":
        bestScore = -10
        for x in range(9):
            if board.values[x] == ' ':
                board.values[x] = letterAI
                score = minimax(board, "min", letterAI, letterH)
                board.values[x] = ' '
                bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = 10
        for x in range(9):
            if board.values[x] == ' ':
                board.values[x] = letterH
                score = minimax(board, "max", letterAI, letterH)
                board.values[x] = ' '
                bestScore = min(bestScore, score)
        return bestScore






if __name__ == "__main__":

    print('Welcome to Tic Tac Toe!')

    values1 = [' ' for x in range(9)]

    board = Board()
    board.print()

    playerLetter = input_player()
    cur_player = ['X', 'O']

    for x in range(9):

        if cur_player[x % 2] == playerLetter:
            print('Your turn')
            move_player(playerLetter, board)
        else:
            print('AI turn')
            move_computer(board, cur_player[x % 2], playerLetter)

        board.print()

        if board.check_win(cur_player[x % 2]):
            if cur_player[x % 2] == playerLetter:
                print('Hooray! You have won the game!')
                raise SystemExit(0)
            else:
                print('The computer has beaten you! You lose.')
                raise SystemExit(0)

    print('The game is a tie!')
