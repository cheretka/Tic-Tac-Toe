import sys



class Move:
    def __init__(self, x, y, x2, y2):
        self.start_x = x
        self.start_y = y
        self.end_x = x2
        self.end_y = y2


class Board:
    def __init__(self):
        self.values = [[' ', 'O', ' ', 'O', ' ', 'O', ' ', 'O'],
                       ['O', ' ', 'O', ' ', 'O', ' ', 'O', ' '],
                       [' ', 'O', ' ', 'O', ' ', 'O', ' ', 'O'],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '],
                       [' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
                       ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ']]


    def print(self):
        print()
        print("       a     b     c     d     e     f     g     h")
        print()
        print("    +-----+-----+-----+-----+-----+-----+-----+-----+")
        for row in range(8):
            sys.stdout.write("{}   |".format(row+1))
            for col in range(8):
                sys.stdout.write("  {}  |".format(self.values[row][col]))
            print()
            print("    +-----+-----+-----+-----+-----+-----+-----+-----+")
        print()
        print("       a     b     c     d     e     f     g     h")


    def check_win(self):
        countx =0
        counto =0
        for row in range(8):
            for col in range(8):
                if self.values[row][col] == 'X':
                    countx +=1
                elif self.values[row][col] == 'O':
                    counto +=1

        if countx==0:
            return 1
        elif counto==0:
            return -1
        else:
            return 0



if __name__ == "__main__":
    board = Board()
    board.print()
