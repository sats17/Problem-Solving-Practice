import pandas as pd
import os


def convertInchToFeet(inch):
    if inch == 0:
        return 0
    return round(inch / 12, 2)


def resolvedInchedValuesToWholeFeetValues(feet, inch):
    if feet == "bad" or inch == "bad":
        return "bad"
    if feet < 0:
        num = abs(feet) + convertInchToFeet(inch)
        return -abs(num)
    return feet + convertInchToFeet(inch)


def unknownOperation(lfeet, linch, bfeet, binch, hfeet, hinch, nos):
    l = resolvedInchedValuesToWholeFeetValues(lfeet, linch)
    b = resolvedInchedValuesToWholeFeetValues(bfeet, binch)
    h = resolvedInchedValuesToWholeFeetValues(hfeet, hinch)
    if l == "bad": l = 1
    if b == "bad": b = 1
    if h == "bad": h = 1
    if nos == "bad": nos = 1
    print("l = ", l, "b = ", b, "h = ", h, "nos = ", nos)
    return l * b * h * nos


def processFile(csvData, output):
    outputArr = []
    csvData.fillna("bad", inplace=True)
    csvData.columns.str.lower()
    totalAnswer = 0
    for data in csvData.itertuples():
        answer = unknownOperation(data.lfeet, data.linch, data.bfeet, data.binch, data.hfeet, data.hinch, data.nos)
        dict = {'name': data.name, 'lfeet': data.lfeet, 'linch': data.linch, 'bfeet': data.bfeet, 'binch': data.binch,
                'hfeet': data.hfeet, 'hinch': data.hinch, 'nos': data.nos, 'answer': answer}
        outputArr.append(dict)
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


# inputFileName = "Book.xlsx"
# outputFileName = "output.xlsx"
# readFile(inputFileName, outputFileName)
dir_list = os.listdir(".")
for i in dir_list:
    if i.__contains__("xlsx") and not i.__contains__("op-"):
        readFile(i, "op-" + i)
