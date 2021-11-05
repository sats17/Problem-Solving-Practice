"""
Here user will feed the data about bills and expenses and who paid how much for particular expense.

function name - getPaymentExchangeInformation
function return - Will return result about who have to pay whom and how much
"""


def getPaymentExchangeInformation(totalMembers, expense):
    print("Total members ", totalMembers)
    print("Expense data ", expense)
    totalBill = calculateTotalBill(expense)
    print("Total bill ", totalBill)
    expectedContriBillForEachMember = calculateExpectedContributionFromEachMember(totalBill, totalMembers)
    print("Each members contri should be ", expectedContriBillForEachMember)
    totalPayFromEachMemberForEachSource = calculateTotalPaymentByEachMembers(expense)
    print("Total members payment for each source ", totalPayFromEachMemberForEachSource)
    names = getNamesFromExpenses(expense)
    zippedPaymentData = zipPaymentAndNames(names, totalPayFromEachMemberForEachSource)
    differentiatedResponse = calculateWhoCanPayWhom(zippedPaymentData, expectedContriBillForEachMember)
    print("Differentiated response ", differentiatedResponse)
    printPaymentInfo(differentiatedResponse)

    return 0


def calculateTotalBill(expense):
    totalBill = 0
    for i in expense:
        totalBill = totalBill + expense[i]["bill"]
    return totalBill


def calculateExpectedContributionFromEachMember(totalBill, member):
    return totalBill / member


def calculateTotalPaymentByEachMembers(expense):
    totalMembersPayment = []
    tempArrayForTotalPayment = []
    for i in expense:
        tempPayment = []
        payments = expense.get(i).get('payments')
        for j in payments:
            tempPayment.append(payments.get(j))
        tempArrayForTotalPayment.append(tempPayment)
    zippedPaymentOfEachMembers = zip(*tempArrayForTotalPayment)
    for i in zippedPaymentOfEachMembers.__iter__():
        eachPayment = 0
        for j in i:
            eachPayment = eachPayment + j
        totalMembersPayment.append(eachPayment)
    return totalMembersPayment


def zipPaymentAndNames(names, payment):
    zippedData = {}
    for name, payment in zip(names, payment):
        zippedData[name] = payment
    print(zippedData)
    return zippedData


def getNamesFromExpenses(expense):
    names = []
    for i in expense:
        paymentList = expense.get(i)
        for j in paymentList.get("payments"):
            names.append(j)
        break
    return names


def calculateWhoCanPayWhom(zippedPaymentData, contriPayment):
    consolidatedResponse = {}
    plus = {}
    minus = {}
    even = {}
    for i in zippedPaymentData:
        tempPayment = zippedPaymentData.get(i)
        if tempPayment > contriPayment:
            plus[i] = tempPayment - contriPayment
        elif tempPayment < contriPayment:
            minus[i] = contriPayment - tempPayment
        else:
            even[i] = 0
    consolidatedResponse['plus'] = plus
    consolidatedResponse['minus'] = minus
    consolidatedResponse['even'] = even
    return consolidatedResponse


def printPaymentInfo(differentiatedResponse):
    plus = differentiatedResponse.get('plus')
    minus = differentiatedResponse.get('minus')
    print("Plus ", plus)
    print("Minus ", minus)
    isTransactionGoing = True
    plusCounter = 0
    minusCounter = 0
    plusList = []
    minusList = []
    # for plus in plus.items():
    #     plusList.append(list(plus))
    # for minus in minus.items():
    #     minusList.append(list(minus))
    print("size", len(plus))
    print("Plus List", plusList)
    print("Minus List", minusList)


"""
{
 merchant: {
    "merchantBill": 123,
    "individualBills":{ "name": bill }
    },
 merchant2: {
    "totalBill": 123,
    "individualBills":{ "name": bill }
    }
}
"""

totalMembers = 4

# expense = {471: [50, 100, 1, 320], 890: [80, 320, 400, 90]}

expense = {"petrol": {"bill": 471, "payments": {"a": 50, "b": 100, "c": 1, "d": 320}},
           "room": {"bill": 890, "payments": {"a": 80, "b": 320, "c": 400, "d": 90}}}
getPaymentExchangeInformation(totalMembers, expense)
print(type(expense))
