def createBoard(size):
    return [[0 for col in range(size)] for row in range(size)]


def createPossibleIndices(size):
    horizontal = [[[0, 0] for col in range(size)] for row in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            horizontal[i][j] = [i, j]
        print(i)
    print(horizontal)
    vertical = [[[0, 0] for col in range(size)] for row in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            vertical[i][j] = horizontal[j][i]
    print(vertical)
    cross = [[[0, 0] for col in range(size)] for row in range(2)]
    m = 0
    n = 0
    for i in range(0, size):
        cross[0][i] = [m, n]
        m += 1
        n += 1
    m = 0
    n = size - 1
    for i in range(0, size):
        cross[1][i] = [m, n]
        m += 1
        n -= 1
    print(cross)

# x = 1
# y = 0


def resultCheck():
    a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print("Current game is ",a[1][1])
    currentColIndex = 1
    currentRowIndex = 1
    size = 3




print(createPossibleIndices(3))
