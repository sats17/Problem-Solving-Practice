class BoardValue:
    def __init__(self, value, nonetBoardIndex, nonetArrayIndex) -> None:
        self.__value = value
        self.__nonetBoardIndex = nonetBoardIndex
        self.__nonetArrayIndex = nonetArrayIndex
        self.__tempValue = None
        self.__isPreset = False
        
    def getValue(self):
        return self.__value
    
    def setValue(self, value):
        self.__value = value
    
    def getNonetBoardIndex(self):
        return self.__nonetBoardIndex
    
    def setNonetBoardIndex(self, nonetBoardIndex):
        self.__nonetBoardIndex = nonetBoardIndex
    
    def getNonetArrayIndex(self):
        return self.__nonetArrayIndex
    
    def setNonetArrayIndex(self, nonetArrayIndex):
        self.__nonetArrayIndex = nonetArrayIndex
    
    def getTempValue(self):
        return self.__tempValue
    
    def setTempValue(self, value):
        self.__tempValue = value
        
    def getIsPreset(self):
        return self.__isPreset
    
    def setIsPreset(self, isPreset):
        self.__isPreset = isPreset
    
    def __repr__(self) -> str:
        return str(self.__value) + " " + str(self.__nonetBoardIndex) + " " + str(self.__nonetArrayIndex) + " " + str(self.__isPreset) 
    
def convertRegularBoardToNonetBoard(regularBoard: list, rowDiv: int, colDiv: int) -> list:
    currentNonetBoardIndex = 1
    nonetBoard = {}
    # Step 1: Increment row using for loop
    for i in range(1, len(regularBoard) + 1):
        originalRowIndex = i - 1
        # Step 2: Increment col using for loop
        for j in range(1, len(regularBoard[originalRowIndex]) + 1):
            originalColIndex = j - 1
            currentObj = regularBoard[originalRowIndex][originalColIndex]
            # Step 3: Update nonetBoard and regularBoard if nonet board created
            if currentNonetBoardIndex in nonetBoard.keys():
                nonetBoard[currentNonetBoardIndex].append(currentObj.getValue())
                currentObj.setNonetBoardIndex(currentNonetBoardIndex)
                currentObj.setNonetArrayIndex(len(nonetBoard[currentNonetBoardIndex]) - 1)
                if currentObj.getValue() != 0:
                    currentObj.setIsPreset(True)
                    
            # Step 4: Create new nonet board if nonet board not created and update regularBoard
            else:
                nonetBoard[currentNonetBoardIndex] = [currentObj.getValue()]
                currentObj.setNonetBoardIndex(currentNonetBoardIndex)
                currentObj.setNonetArrayIndex(len(nonetBoard[currentNonetBoardIndex]) - 1)
            
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

def sudokuSolver(regularBoard: list, rowDiv: int, colDiv: int) -> list:
    nonetBoard = convertRegularBoardToNonetBoard(regularBoard, rowDiv, colDiv)
    print("Nonet board ",nonetBoard)
    print("Regular board ")
    for i in regularBoard:
        print(i)
    for regularBoardRowIndex in range(0, len(regularBoard)):
        regularBoardRow = regularBoard[regularBoardRowIndex]
        currentValue = None
        isBackwardFlowStarted = False
        swappedTempValue = None
        unfittedIndex = None
        for regularBoardColumnIndex in range(0, len(regularBoardRow)):
            regularBoardColumn = regularBoardRow[regularBoardColumnIndex]
            value = regularBoardColumn.getValue()
            
            if isBackwardFlowStarted == False:
                if value != 0:
                    # Skipping value which already present in board
                    continue
                else:
                    if validateAndAppendValue(regularBoard, nonetBoard, value, regularBoardRowIndex, regularBoardColumnIndex):
                        break
                    else:
                        print('test')
            if regularBoardColumn.getValue() != 0:
                print("Value is ", regularBoardColumn.getValue())
                print("Skipping this value")
                continue
            
def validateAndAppendValue(regularBoard, nonetBoard, value, rowIndex, colIndex):
    isValid = False
    currentBoardValue = regularBoard[rowIndex][colIndex]
    if value is not None:
        # Validate row
        for boardValue in regularBoard[rowIndex]:
            if boardValue.getValue() == value:
                return False
        isValid = True
        
        # Validate column
        for row in regularBoard:
            if row[colIndex].getValue() == value:
                return False
        isValid = True
        
        # Validate nonet
        boardIndex = currentBoardValue.getNonetBoardIndex()
        arrayIndex = currentBoardValue.getNonetArrayIndex()
        if boardIndex in nonetBoard.keys():
            for boardValue in nonetBoard[boardIndex]:
                if boardValue == value:
                    return False
        isValid = True
        regularBoard[rowIndex][colIndex].setValue(value)
        nonetBoard[boardIndex][arrayIndex] = value
        return isValid
    else:
        # Need to check in single iteration of 1 to 9, how can I validate all three.
        return None

if __name__ == "__main__":
    regularBoard = generateRegularBoard(9, 9)
    regularBoard[0][2].setValue(5)
    regularBoard[2][2].setValue(7)
    regularBoard[0][5].setValue(9)
    regularBoard[0][8].setValue(1)
    regularBoard[1][0].setValue(6)
    regularBoard[2][0].setValue(1)
    regularBoard[2][0].setValue(1)
    regularBoard[8][8].setValue(9)
    nonetBoard = convertRegularBoardToNonetBoard(regularBoard, 3, 3)
    print(nonetBoard)
    print("############################################")
    for i in regularBoard:
        print(i)
    print("after")
    print(validateAndAppendValue(regularBoard, nonetBoard, 7, 0, 0))
    print(nonetBoard)
    print("############################################")
    for i in regularBoard:
        print(i)
    # print(validateAndAppendValue(regularBoard, nonetBoard, 6, 0, 0))
    # sudokuSolver(regularBoard, 9, 9)
    
    # Next action
    # for validateAndAppendValue method need to complete else part, and also need to check if we can reuse existing logic also which written

