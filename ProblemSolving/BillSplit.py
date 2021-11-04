"""
Here user will feed the data about bills and expenses and who paid how much for particular expense.

function name - getPaymentExchangeInformation
function return - Will return result about who have to pay whom and how much
"""


def getPaymentExchangeInformation(totalMembers, expense):
    print("Total members ", totalMembers)
    print("Expense data ", expense)
    totalBills = calculateTotalBill(expense)
    print("Total bill ", totalBills)
    # contriBillForEachMember = calculateEachMemberContribution(totalBill, totalMembers)
    # print("Each members contri should be ", contriBillForEachMember)
    # totalPayFromEachMemberForEachSource = calculateTotalPaymentFromEachMembers(expense, totalMembers)
    # print("Total members payment for each source ", totalPayFromEachMemberForEachSource)

    return 0


def calculateTotalBill(expense):
    totalBill = 0
    for i in expense:
        totalBill = totalBill + expense[i]["bill"]
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

#expense = {471: [50, 100, 1, 320], 890: [80, 320, 400, 90]}

expense = {"petrol": {"bill": 471, "payments": {"a": 50, "b": 100, "c": 1, "d": 320}},
           "room": {"bill": 890, "payments": {"a": 80, "b": 320, "c": 400, "d": 90}}}
getPaymentExchangeInformation(totalMembers, expense)
print(type(expense))
