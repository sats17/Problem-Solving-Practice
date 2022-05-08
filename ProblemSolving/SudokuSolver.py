class BoardValue:
    def __init__(self, value, nonetBoardIndex, nonetArrayIndex, regularBoardRowIndex, regularBoardColIndex) -> None:
        self.__value = value
        self.__nonetBoardIndex = nonetBoardIndex
        self.__nonetArrayIndex = nonetArrayIndex
        self.__regularBoardRowIndex = regularBoardRowIndex
        self.__regularBoardColIndex = regularBoardColIndex
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
        
    def getRegularBoardRowIndex(self):
        return self.__regularBoardRowIndex
    
    def getRegularBoardColIndex(self):
        return self.__regularBoardColIndex
    
    def __repr__(self) -> str:
        return str(self.__value)
    # + " " + str(self.__nonetBoardIndex) + " " + str(self.__nonetArrayIndex) + " " + str(self.__isPreset) + " " + str(self.__regularBoardRowIndex) + " " + str(self.__regularBoardColIndex)
    
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
            innerBoard.append(BoardValue(0, None, None, i, j))
        regularBoard.append(innerBoard)
    return regularBoard

def sudokuSolver(regularBoard: list, rowDiv: int, colDiv: int) -> list:
    nonetBoard = convertRegularBoardToNonetBoard(regularBoard, 3, 3)
    print("Nonet board ",nonetBoard)
    print("Regular board ")
    # for i in regularBoard:
    #     print(i)
    for regularBoardRowIndex in range(0, len(regularBoard)):
        regularBoardRow = regularBoard[regularBoardRowIndex]
        isBackwardFlowStarted = False
        unfittedValue = None
        regularBoardColumnIndex = 0
        while regularBoardColumnIndex < len(regularBoardRow):
            print("regularBoardRowIndex: ", regularBoardRowIndex, "regularBoardColumnIndex: ", regularBoardColumnIndex)
            for i in regularBoard:
                print(i)
            regularBoardColumn = regularBoardRow[regularBoardColumnIndex]
            value = regularBoardColumn.getValue()
            
            if isBackwardFlowStarted == False:
                if value != 0:
                    # Skipping value which already present in board
                    regularBoardColumnIndex += 1
                else:
                    if validateAndAppendValue(regularBoard, nonetBoard, None, regularBoardRowIndex, regularBoardColumnIndex):
                        regularBoardColumnIndex += 1
                    else:
                        print("For row " + str(regularBoardRowIndex) + " col " + str(regularBoardColumnIndex) + " value is not fitting, so backward flow started")
                        regularBoardColumnIndex -= 1
                        isBackwardFlowStarted = True
                        unfittedValue = regularBoardColumn
                        # for i in regularBoard:
                        #     print(i)
            else:
                if regularBoardColumn.getIsPreset() == True:
                    regularBoardColumnIndex -= 1
                else:
                    regularBoardColumn.setTempValue(regularBoardColumn.getValue())
                    regularBoardColumn.setValue(0)
                    nonetBoard[regularBoardColumn.getNonetBoardIndex()][regularBoardColumn.getNonetArrayIndex()] = 0
                    
                    if validateAndAppendValue(regularBoard, nonetBoard, regularBoardColumn.getTempValue(), unfittedValue.getRegularBoardRowIndex(), unfittedValue.getRegularBoardColIndex()):
                        print("Value fitted in ", regularBoardColumn.getRegularBoardRowIndex(), regularBoardColumn.getRegularBoardColIndex())
                        isBackwardFlowStarted = False
                        unfittedValue = None
                        regularBoardColumn.setTempValue(None)
                        print(regularBoardColumnIndex)
                        print(regularBoardRow[regularBoardColumnIndex])
                        # for i in regularBoard:
                        #     print(i)
                    else:
                        regularBoardColumn.setValue(regularBoardColumn.getTempValue())
                        regularBoardColumn.setTempValue(None)
                        nonetBoard[regularBoardColumn.getNonetBoardIndex()][regularBoardColumn.getNonetArrayIndex()] = regularBoardColumn.getValue()
                        regularBoardColumnIndex -= 1
                    # print('Inside else part of backward flow')
                    # print(regularBoardColumnIndex)
            # if regularBoardColumn.getValue() != 0:
            #     print("Value is ", regularBoardColumn.getValue())
            #     print("Skipping this value")
            #     continue
            
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
        for i in range(1, 10):
            if validateAndAppendValue(regularBoard, nonetBoard, i, rowIndex, colIndex):
                return True
        return False
    
def testData(regularBoard):
    test1 = [{'value': 2, 'row': 0, 'col': 3}, 
             {'value': 6, 'row': 0, 'col': 4}, 
             {'value': 7, 'row': 0, 'col': 6}, 
             {'value': 1, 'row': 0, 'col': 8}, 
             {'value': 6, 'row': 1, 'col': 0}, 
             {'value': 8, 'row': 1, 'col': 1}, 
             {'value': 7, 'row': 1, 'col': 4}, 
             {'value': 9, 'row': 1, 'col': 7}, 
             {'value': 1, 'row': 2, 'col': 0}, 
             {'value': 9, 'row': 2, 'col': 1}, 
             {'value': 4, 'row': 2, 'col': 5},
             {'value': 5, 'row': 2, 'col': 6}, 
             {'value': 8, 'row': 3, 'col': 0}, 
             {'value': 2, 'row': 3, 'col': 1},
             {'value': 1, 'row': 3, 'col': 3}, 
             {'value': 4, 'row': 3, 'col': 7},
             {'value': 4, 'row': 4, 'col': 2},
             {'value': 6, 'row': 4, 'col': 3},
             {'value': 2, 'row': 4, 'col': 5},
             {'value': 9, 'row': 4, 'col': 6},
             {'value': 5, 'row': 5, 'col': 1},
             {'value': 3, 'row': 5, 'col': 5},
             {'value': 2, 'row': 5, 'col': 7},
             {'value': 8, 'row': 5, 'col': 8},
             {'value': 9, 'row': 6, 'col': 2},
             {'value': 3, 'row': 6, 'col': 3}, 
             {'value': 7, 'row': 6, 'col': 7},
             {'value': 4, 'row': 6, 'col': 8}, 
             {'value': 4, 'row': 7, 'col': 1},
             {'value': 5, 'row': 7, 'col': 4},
             {'value': 3, 'row': 7, 'col': 7},
             {'value': 6, 'row': 7, 'col': 8},
             {'value': 7, 'row': 8, 'col': 0},
             {'value': 3, 'row': 8, 'col': 2},
             {'value': 1, 'row': 8, 'col': 4}, 
             {'value': 8, 'row': 8, 'col': 5}]
    
    
    test2 = [{'value': 2, 'row': 0, 'col': 3}]
    test3 = [{'value': 7, 'row': 1, 'col': 2}, {'value': 4, 'row': 8, 'col': 4}, {'value': 5, 'row': 4, 'col': 2}]
    for dictData in test3:
        rowIndex = dictData['row']
        colIndex = dictData['col']
        value = dictData['value']
        regularBoard[rowIndex][colIndex].setValue(value)     
        
def getUserInput(regularBoard):
    isExit = False
    savedInput = []
    while not isExit:
        dic = {}
        inputValue = input("Enter value(Format: 'value, rowIndex, colIndex'): Enter 'exit' to exit: ")
        if inputValue == "exit":
            isExit = True
        else:
            inputArr = inputValue.split(",")
            value = int(inputArr[0])
            rowIndex = int(inputArr[1])
            colIndex = int(inputArr[2])
            regularBoard[rowIndex][colIndex].setValue(value)
            dic = {'value': value, 'row': rowIndex, 'col': colIndex}
            savedInput.append(dic)
    print(savedInput) 
    
def printDashBoard():
    print("=" * 100)
    print(" " * 35 + "Welcome to Sudoku Solver")
    

if __name__ == "__main__":
            
    printDashBoard()
    regularBoard = generateRegularBoard(9, 9)
    getUserInput(regularBoard)
    #testData(regularBoard)
    for i in regularBoard:
        print(i)
    sudokuSolver(regularBoard, 9, 9)
    print('=' * 100)
    print(" " * 35 + "Sudoku Solver is done")
    print('=' * 100)
    print(" " * 35 + "Sudoku Board")
    print(regularBoard)
    for i in regularBoard:
        print(i)
    
    # testData(regularBoard)
    # nonetBoard = convertRegularBoardToNonetBoard(regularBoard, 3, 3)
    
    # sudokuSolver(regularBoard, 9, 9)
    # print("After solving")
    # for i in regularBoard:
    #     print(i)
    # Next action
    # Failing with Enter 'exit' to exit: 7,1,2
# Enter value(Format: 'value, rowIndex, colIndex'): Enter 'exit' to exit: 4,8,4
# Enter value(Format: 'value, rowIndex, colIndex'): Enter 'exit' to exit: 5,4,2
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [4, 5, 7, 1, 9, 8, 2, 3, 6]
# [6, 8, 9, 2, 3, 7, 1, 4, 5]
# [2, 1, 4, 3, 6, 5, 8, 9, 7]
# [3, 6, 5, 7, 8, 9, 4, 1, 2]
# [7, 9, 8, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 4, 0, 0, 0, 0]
