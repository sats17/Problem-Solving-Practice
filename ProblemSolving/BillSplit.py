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
    contriBillForEachMember = calculateEachMemberContribution(totalBill, totalMembers)
    print("Each members contri should be ",contriBillForEachMember)
    totalPayFromEachMemberForEachSource = calculateTotalPaymentFromEachMembers(expense, totalMembers)
    print("Total members payment for each source ", totalPayFromEachMemberForEachSource)

    return 0


def calculateTotalBill(expense):
    totalBill = 0
    for i in expense:
        totalBill = totalBill + i
    return totalBill


def calculateEachMemberContribution(totalBill, member):
    return totalBill / member


def calculateTotalPaymentFromEachMembers(expense, totalMembers):
    totalMembersPayment = []
    tempArrayForTotalPayment = []
    for i in expense:
        tempArrayForTotalPayment.append(expense.get(i))
    print(tempArrayForTotalPayment)
    zippedPaymentOfEachMembers = zip(*tempArrayForTotalPayment)
    for i in zippedPaymentOfEachMembers.__iter__():
        eachPayment = 0
        for j in i:
            eachPayment = eachPayment + j;
        totalMembersPayment.append(eachPayment)
    return totalMembersPayment


totalMembers = 4

expense = {471: [50, 100, 1, 320], 890: [80, 320, 400, 90]}
getPaymentExchangeInformation(totalMembers, expense)
print(type(expense))
