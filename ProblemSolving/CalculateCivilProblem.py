import pandas as pd


def convertInchToFeet(inch):
    if inch == 0:
        return 0
    return round(inch / 12, 2)


def resolvedInchedValuesToWholeFeetValues(feet, inch):
    if feet == -999 or inch == -999:
        return -1
    return feet + convertInchToFeet(inch)


def unknownOperation(lfeet, linch, bfeet, binch, hfeet, hinch, nos):
    l = resolvedInchedValuesToWholeFeetValues(lfeet, linch)
    b = resolvedInchedValuesToWholeFeetValues(bfeet, binch)
    h = resolvedInchedValuesToWholeFeetValues(hfeet, hinch)
    if nos == -999:
        nos = -1
    if l == -1: l = 1
    if b == -1: b = 1
    if h == -1: h = 1
    if nos == -1: nos = 1
    return l * b * h * nos


def processFile(csvData, output):
    outputArr = []
    csvData.fillna(-999, inplace=True)
    for data in csvData.itertuples():
        answer = unknownOperation(data.lfeet, data.linch, data.bfeet, data.binch, data.hfeet, data.hinch, data.nos)
        dict = {'name': data.name, 'lfeet': data.lfeet, 'linch': data.linch, 'bfeet': data.bfeet, 'binch': data.binch,
                'hfeet': data.hfeet, 'hinch': data.hinch, 'nos': data.nos, 'answer': answer}
        outputArr.append(dict)
    pd.DataFrame(outputArr).to_csv(output, index=False)
    print("Done")


def readFile(input, output):
    csvData = pd.read_csv(input)
    print("File read complete")
    processFile(csvData, output)
    print("Processing done please see output.csv file")


inputFileName = "input.csv"
outputFileName = "output3.csv"
readFile(inputFileName, outputFileName)
