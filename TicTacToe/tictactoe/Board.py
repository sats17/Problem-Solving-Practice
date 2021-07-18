from TicTacToe.tictactoe.Response import Response
from TicTacToe.tictactoe.TicTacToeI import TicTacToeI


class Board(TicTacToeI):
    __size = None
    __dashBoard = None
    __horizontalPossibility = None
    __verticalPossibility = None
    __crossPossibility = None

    def __init__(self, size):
        self.__size = size
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

    def capture_move(self, index: list, value: str) -> object:
        response_obj = Response()
        print(self.__size)
        print(index[0])
        print(isinstance(value, str))
        if not isinstance(value, str) or value.lower() not in self.get_values():
            print("Error occurs while validating value")
            return response_obj.is_valid_value(False, "Invalid value entered, please enter either x or o").build()
        if not isinstance(index, list):
            return response_obj.is_valid_index(False, "Invalid index entered").build()
        if index[0] < 0 or index[0] > self.__size - 1 or index[1] < 0 or index[1] > self.__size - 1:
            return response_obj.is_valid_index(False, "Invalid index entered").build()
        if self.__dashBoard[index[0]][index[1]] != 0:
            return response_obj.is_valid_index(False, "Invalid index entered").build()
        self.__dashBoard[index[0]][index[1]] = self.get_values().get(value.lower())
        print(self.__dashBoard)
        print("Validation success")
        return response_obj.build()


a = Board(3)
print(a.get_dashboard())
print(a.capture_move([1, 1], "o"))
print(a.capture_move([1, 1], "o"))
