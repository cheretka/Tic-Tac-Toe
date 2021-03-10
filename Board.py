
class Board:
    def __init__(self):
        self.values = [' ' for x in range(9)]
        self.stack = []
        self.current_player = "X"

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

    def check_win(self):
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        # if win x return 1
        curPlayer = 'X'
        for x in soln:
            counter = 0
            for ind in x:
                if self.values[ind - 1] == curPlayer:
                    counter += 1
            if counter == 3:
                return 1

        # if win o return -1
        curPlayer = 'O'
        for x in soln:
            counter = 0
            for ind in x:
                if self.values[ind - 1] == curPlayer:
                    counter += 1
            if counter == 3:
                return -1

        # if the game continues return 2
        for y in self.values:
            if y == " ":
                return 2

        # if game over return 0
        return 0

    def get_possible_moves(self):
        player = self.current_player

        list = []
        for x in range(9):
            if self.values[x] == ' ':
                list.append([x, player])
        return list

    def make_move(self, move):
        if self.values[move[0]] == ' ':
            self.stack.append(self.values.copy())
            self.values[move[0]] = move[1]
            self.switch_player()
            return True
        return False

    def undo_move(self):
        self.values = self.stack.pop()
        self.switch_player()
        pass

    def switch_player(self):
        self.current_player = 'O' if self.current_player == "X" else 'X'

