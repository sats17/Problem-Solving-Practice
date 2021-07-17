class Board(object):
    dashBoard = None
    horizontalPossibility = None
    verticalPossibility = None
    crossPossibility = None

    def __init__(self, size):
        self.dashBoard = [[0 for col in range(size)] for row in range(size)]
        self.createHorizontalPossibility(size)
        self.createVerticalPossibility(size)
        self.createCrossPossibility(size)

    def createHorizontalPossibility(self, size):
        self.horizontalPossibility = [[[0, 0] for col in range(size)] for row in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                self.horizontalPossibility[i][j] = [i, j]

    def createVerticalPossibility(self, size):
        self.verticalPossibility = [[[0, 0] for col in range(size)] for row in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                self.verticalPossibility[i][j] = self.horizontalPossibility[j][i]

    def createCrossPossibility(self, size):
        self.crossPossibility = [[[0, 0] for col in range(size)] for row in range(2)]
        m = 0
        n = 0
        for i in range(0, size):
            self.crossPossibility[0][i] = [m, n]
            m += 1
            n += 1
        m = 0
        n = size - 1
        for i in range(0, size):
            self.crossPossibility[1][i] = [m, n]
            m += 1
            n -= 1