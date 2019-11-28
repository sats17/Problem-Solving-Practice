row = 3
col = 5
bombs = [[0,2],[1,1]]

def Sweeper(bombs,row,col):
    board = [[0 for x in range(col)]for y in range(row)]
    print(bombs)
    length = len(bombs)
    for i in range(length):
        board[bombs[i][0]][bombs[i][1]] = -1
    print(board)
    for i in range(row):
        for j in range(col):
            if(board[i][j] == -1):
                continue
            count = 0
            #print("i = ",i," j = ",j)
            for s in range(i-1,i+2):
                for p in range(j -1, j + 2):
                    if(s < 0 or p < 0 or s >= row or p >= col):
                        continue
                   # print("S ",s," p ",p)
                    if(board[s][p] ==  -1):
                        count+=1
            board[i][j] = count




    return board

# i = 2
# j = 4
# for s in range(i - 1, i + 2):
#     for p in range(j - 1, j + 2):
#         print(s)
print(Sweeper(bombs,row,col))