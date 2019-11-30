row = 4
col = 4
bombs = [[0,0],[3,3]]

def boardCreator(bombs,row,col):
    board = [[0 for x in range(col)]for y in range(row)]
    length = len(bombs)
    for i in range(length):
        rowPos = bombs[i][0]
        colPos = bombs[i][1]
        board[rowPos][colPos] = -1
        for s in range(rowPos - 1, rowPos + 2):
            for p in range(colPos - 1, colPos + 2):
                if (s < 0 or p < 0 or s >= row or p >= col):
                    continue
                if (board[s][p] == -1):
                    continue
                board[s][p]+=1

    print(board)

    return board

def whenUserClick(rowPos,colPos):
    Board = boardCreator(bombs,row,col)
    if(Board[rowPos][colPos] == 0):
        Board[rowPos][colPos] = -2
        graphTraverse(Board,rowPos,colPos)
    return Board


def graphTraverse(Board,rowPos,colPos):
    if(Board[rowPos][colPos] == -1):
        return "Bomb Found"
    if(Board[rowPos][colPos] != 0):
        Board[rowPos][colPos] = -2
        return Board
    for s in range(rowPos - 1, rowPos + 2):
        for p in range(colPos - 1, colPos + 2):
            if (s < 0 or p < 0 or s >= row or p >= col):
                continue
            elif (Board[s][p] != 0):
                continue
            else:
                Board[rowPos][colPos] = -2
                graphTraverse(Board,s,p)
    return Board



Board = boardCreator(bombs,row,col)
print(graphTraverse(Board,3,2))