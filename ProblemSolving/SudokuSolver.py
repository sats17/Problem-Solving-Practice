class BoardValue:
    def __init__(self, value, nonetBoardIndex, nonetArrayIndex) -> None:
        self.value = value
        self.nonetBoardIndex = nonetBoardIndex
        self.nonetArrayIndex = nonetArrayIndex
        
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
    
    def getNonetBoardIndex(self):
        return self.nonetBoardIndex
    
    def getNonetArrayIndex(self):
        return self.nonetArrayIndex
    
    def __repr__(self) -> str:
        return str(self.value) + " " + str(self.nonetBoardIndex) + " " + str(self.nonetArrayIndex)
    
    
def convertRegularBoardToNonetBoard(regularBoard: list, rowDiv: int, colDiv: int) -> list:
    colCounter = 1
    currentNonetBoardIndex = 1
    nonetBoard = {}
    # Step 1: Increment row using for loop
    for i in range(1, len(regularBoard) + 1):
        originalRowIndex = i - 1
        # Step 2: Increment col using for loop
        for j in range(1, len(regularBoard[originalRowIndex]) + 1):
            originalColIndex = j - 1
            
            # Step 3: Update nonetBoard and regularBoard if nonet board created
            if currentNonetBoardIndex in nonetBoard.keys():
                nonetBoard[currentNonetBoardIndex].append(regularBoard[originalRowIndex][originalColIndex].getValue())
                regularBoard[originalRowIndex][originalColIndex].nonetBoardIndex = currentNonetBoardIndex
                regularBoard[originalRowIndex][originalColIndex].nonetArrayIndex = len(nonetBoard[currentNonetBoardIndex]) - 1
            # Step 4: Create new nonet board if nonet board not created and update regularBoard
            else:
                nonetBoard[currentNonetBoardIndex] = [regularBoard[originalRowIndex][originalColIndex].getValue()]
                regularBoard[originalRowIndex][originalColIndex].nonetBoardIndex = currentNonetBoardIndex
                regularBoard[originalRowIndex][originalColIndex].nonetArrayIndex = 0
            
            # Step 5: Validation of col, which later decide NontetBoardIndex
            if j % colDiv == 0 and j != 9:
                currentNonetBoardIndex += 1

        # Step 4: Validation of row, which later decide NontetBoardIndex should be incremented or switch it back to first nonet board
        # while row switching
        if i % rowDiv == 0:
            print(i)
            currentNonetBoardIndex += 1
        else:
            if currentNonetBoardIndex != 1:
                currentNonetBoardIndex -= 2
    return nonetBoard

def generateRegularBoard(rowDiv: int, colDiv: int) -> list:
    regularBoard = []
    for i in range(rowDiv):
        innerBoard = []
        for j in range(colDiv):
            innerBoard.append(BoardValue(0, None, None))
        regularBoard.append(innerBoard)
    return regularBoard

if __name__ == "__main__":
    regularBoard = generateRegularBoard(9, 9)
    regularBoard[0][2].setValue(5)
    regularBoard[0][5].setValue(9)
    regularBoard[0][8].setValue(1)
    regularBoard[1][0].setValue(6)
    regularBoard[2][0].setValue(1)
    regularBoard[2][0].setValue(1)
    regularBoard[8][8].setValue(9)
    
    nonetBoard = convertRegularBoardToNonetBoard(regularBoard, 3, 3)
    for i in regularBoard:
        print(i)
    print(nonetBoard)

