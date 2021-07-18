from TicTacToe.tictactoe.TicTacToeI import TicTacToeI


class Board(TicTacToeI):
    __dashBoard = None
    __horizontalPossibility = None
    __verticalPossibility = None
    __crossPossibility = None

    def __init__(self, size):
        self.__dashBoard = [[0 for col in range(size)] for row in range(size)]
        self.__createHorizontalPossibility(size)
        self.__createVerticalPossibility(size)
        self.__createCrossPossibility(size)

    def get_dashboard(self):
        return self.__dashBoard

    def __createHorizontalPossibility(self, size):
        self.__horizontalPossibility = [[[0, 0] for col in range(size)] for row in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                self.__horizontalPossibility[i][j] = [i, j]

    def __createVerticalPossibility(self, size):
        self.__verticalPossibility = [[[0, 0] for col in range(size)] for row in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                self.__verticalPossibility[i][j] = self.__horizontalPossibility[j][i]

    def __createCrossPossibility(self, size):
        self.__crossPossibility = [[[0, 0] for col in range(size)] for row in range(2)]
        m = 0
        n = 0
        for i in range(0, size):
            self.__crossPossibility[0][i] = [m, n]
            m += 1
            n += 1
        m = 0
        n = size - 1
        for i in range(0, size):
            self.__crossPossibility[1][i] = [m, n]
            m += 1
            n -= 1

    def capture_move(self, index: str, value: str) -> object:
        if not isinstance(value, str) or value.lower() != 'x' or value.lower() != 'o':
            return False


a = Board(3)
print(a.get_dashboard())
print(a.capture_move(2, 'x'))
