import pandas as pd
import os


def convertInchToFeet(inch):
    if inch == 0:
        return 0
    return round(inch / 12, 2)


def resolvedInchedValuesToWholeFeetValues(feet, inch):
    if feet == "bad" or inch == "bad":  # Have this validation for backward compatibilty
        return 1
    if feet < 0:
        num = abs(feet) + convertInchToFeet(inch)
        return -abs(num)
    return feet + convertInchToFeet(inch)


def unknownOperationScatterd(lfeet, linch, bfeet, binch, hfeet, hinch, nos):
    l = resolvedInchedValuesToWholeFeetValues(lfeet, linch)
    b = resolvedInchedValuesToWholeFeetValues(bfeet, binch)
    h = resolvedInchedValuesToWholeFeetValues(hfeet, hinch)
    if l == "bad": l = 1
    if b == "bad": b = 1
    if h == "bad": h = 1
    if nos == "bad": nos = 1
    print("l = ", l, "b = ", b, "h = ", h, "nos = ", nos)
    return l * b * h * nos


def unknownOperation(L, B, H, N):
    updatedL = initialValidator(L)
    updatedB = initialValidator(B)
    updatedH = initialValidator(H)
    if N == "bad": N = 1
    print("l = ", updatedL, "b = ", updatedB, "h = ", updatedH, "N = ", N)
    return updatedL * updatedB * updatedH * N


def initialValidator(value):
    if value != "bad":
        if type(value) != int:
            seperatedArray = value.split(",")
            feet = seperatedArray[0]
            inch = seperatedArray[1]
            updatedValue = resolvedInchedValuesToWholeFeetValues(float(feet), float(inch))
        else:
            updatedValue = resolvedInchedValuesToWholeFeetValues(float(value), 0)
    else:
        updatedValue = 1
    return updatedValue


def processFile(csvData, output):
    outputArr = []
    csvData.fillna("bad", inplace=True)
    csvData.columns.str.lower()
    totalAnswer = 0
    for data in csvData.itertuples():
        if isFileReduced:
            answer = round(unknownOperation(data.L, data.B, data.H, data.N), 3)
            print("Answer = ",answer)
            dictOutput = {'name': data.name, 'L': data.L, 'B': data.B, 'H': data.H, 'N': data.N, 'answer': answer}
        else:
            answer = round(
                unknownOperationScatterd(data.lfeet, data.linch, data.bfeet, data.binch, data.hfeet, data.hinch,
                                         data.nos), 3)
            print("Answer ",answer)
            dictOutput = {'name': data.name, 'lfeet': data.lfeet, 'linch': data.linch, 'bfeet': data.bfeet,
                          'binch': data.binch,
                          'hfeet': data.hfeet, 'hinch': data.hinch, 'nos': data.nos, 'answer': answer}
        outputArr.append(dictOutput)
        totalAnswer = totalAnswer + answer
    answerDict = {'answer': totalAnswer}
    outputArr.append(answerDict)
    pd.DataFrame(outputArr).to_excel(output, index=False)
    print("Done")


def readFile(input, output):
    # csvData = pd.read_csv(input)
    print("Processing started for file ", input)
    csvData = pd.read_excel(input, sheet_name="Sheet1")
    print("File read complete")
    processFile(csvData, output)
    print("Processing done please see ", output, " file \n")


isFileReduced = True
# inputFileName = "Book1.xlsx"
# outputFileName = "output1.xlsx"
# readFile(inputFileName, outputFileName)
dir_list = os.listdir(".")
for i in dir_list:
    if i.__contains__("xlsx") and not i.__contains__("op-"):
        readFile(i, "op-" + i)
