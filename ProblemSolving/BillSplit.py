"""
Here user will feed the data about bills and expenses and who paid how much for particular expense.

function name - getPaymentExchangeInformation
function return - Will return result about who have to pay whom and how much
"""


def getPaymentExchangeInformation(totalMembers, expense):
    print("Total members ", totalMembers)
    print("Expense data ", expense)
    names = extractMembersNames(expense)
    totalBill = calculateTotalBill(expense)
    print("Total bill ", totalBill)
    expectedContributionBillFromEachMember = calculateExpectedContributionFromEachMember(totalBill, totalMembers)
    print("Expected contribution from each members ", expectedContributionBillFromEachMember)
    totalPayFromEachMemberForEachSource = calculateTotalPaymentByEachMembers(expense)
    print("Total members payment for each source ", totalPayFromEachMemberForEachSource)
    zippedPaymentData = zipPaymentAndNames(names, totalPayFromEachMemberForEachSource)
    differentiatedResponse = differentiateCreditorAndDebtor(zippedPaymentData, expectedContributionBillFromEachMember)
    print("Differentiated response ", differentiatedResponse)
    events = generateResolvedContributionEvents(differentiatedResponse)

    return events


def calculateTotalBill(expense):
    totalBill = 0
    for i in expense:
        totalBill = totalBill + expense[i]["bill"]
    return totalBill


def calculateExpectedContributionFromEachMember(totalBill, member):
    return totalBill / member


def calculateTotalPaymentByEachMembers(expense):
    totalMembersPaymentArray = []
    tempArrayForTotalPayment = []
    for i in expense:
        tempPayment = []
        payments = expense.get(i).get('payments')
        for names in payments:
            tempPayment.append(payments.get(names))
        tempArrayForTotalPayment.append(tempPayment)
    zippedPaymentOfEachMembers = zip(*tempArrayForTotalPayment)  # zip arrays present in tempArrayForTotalPayment
    for eachMemberPaymentArray in zippedPaymentOfEachMembers.__iter__():
        totalPaymentByEachMember = 0
        for payment in eachMemberPaymentArray:
            totalPaymentByEachMember = totalPaymentByEachMember + payment
        totalMembersPaymentArray.append(totalPaymentByEachMember)
    return totalMembersPaymentArray


def zipPaymentAndNames(names, payment):
    zippedData = {}
    for name, payment in zip(names, payment):
        zippedData[name] = payment
    return zippedData


def extractMembersNames(expense):
    names = []
    for i in expense:
        paymentList = expense.get(i)
        for j in paymentList.get("payments"):
            names.append(j)
        break
    return names


def differentiateCreditorAndDebtor(zippedPaymentData, expectedContributionBill):
    consolidatedResponse = {}
    creditor = {}
    debtor = {}
    even = {}
    for name in zippedPaymentData:
        paymentFromMember = zippedPaymentData.get(name)
        if paymentFromMember < expectedContributionBill:
            creditor[name] = expectedContributionBill - paymentFromMember
        elif paymentFromMember > expectedContributionBill:
            debtor[name] = paymentFromMember - expectedContributionBill
        else:
            even[name] = 0
    consolidatedResponse['creditor'] = creditor
    consolidatedResponse['debtor'] = debtor
    consolidatedResponse['even'] = even
    return consolidatedResponse


def generateResolvedContributionEvents(differentiatedResponse):
    events = []
    creditor = differentiatedResponse.get('creditor')
    debtor = differentiatedResponse.get('debtor')
    print("Creditors ", creditor)
    print("Debtor ", debtor)
    creditCounter = 0
    debtCounter = 0
    creditorsList = []
    debtorsList = []
    for creditor in creditor.items():
        creditorsList.append(list(creditor))
    for debtor in debtor.items():
        debtorsList.append(list(debtor))

    while True:
        # Running creditorList and debtorList simultaneously, once operations on both list completed then breaking
        # this loop to avoid array index out of bound errors
        if creditCounter > len(creditorsList) - 1 and debtCounter > len(debtorsList) - 1:
            break
        print("Credit counter ", creditCounter)
        print("Debit counter", debtCounter)
        currentCreditor = creditorsList[creditCounter]
        currentDebtor = debtorsList[debtCounter]
        # When Credit person have less amount that debit person, then creditor pay all his amount to debtor
        if currentCreditor[1] != 0 and currentCreditor[1] < currentDebtor[1]:
            events.append(eventGenerator(currentCreditor[0], currentCreditor[1], currentDebtor[0]))
            exchangeValue = creditorsList[creditCounter][1]
            creditorsList[creditCounter][1] = 0
            debtorsList[debtCounter][1] = debtorsList[debtCounter][1] - exchangeValue
            creditCounter = creditCounter + 1  # Increase counter to iterate to next debtor
        # When debit person have less amount that credit person, then creditor will pay only amount that debtor have
        if currentDebtor[1] != 0 and currentCreditor[1] > currentDebtor[1]:
            events.append(eventGenerator(currentCreditor[0], currentDebtor[1], currentDebtor[0]))
            exchangeValue = debtorsList[debtCounter][1]
            debtorsList[debtCounter][1] = 0
            creditorsList[creditCounter][1] = creditorsList[creditCounter][1] - exchangeValue
            debtCounter = debtCounter + 1  # Increase counter to iterate to next debtor
        # When credit person and debit person have equal amount, then creditor will pay whatever he have to debtor
        if currentDebtor[1] != 0 and currentCreditor[1] != 0 and currentCreditor[1] == currentDebtor[1]:
            events.append(eventGenerator(currentCreditor[0], currentCreditor[1], currentDebtor[0]))
            creditorsList[creditCounter][1] = 0
            debtorsList[debtCounter][1] = 0
            debtCounter = debtCounter + 1  # Increase counter to iterate to next debtor
            creditCounter = creditCounter + 1  # Increase counter to iterate to next creditor
        print("Updated creditors list", creditorsList)
        print("Updated debtors list ", debtorsList)
    return events


def eventGenerator(creditorName, amount, debtorName):
    return str(creditorName) + " will pay " + str(amount) + " to " + str(debtorName)


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

if __name__ == "__main__":
    totalMembers = 4
    expense = {"petrol": {"bill": 470, "payments": {"a": 470, "b": 0, "c": 0, "d": 0}},
               "room": {"bill": 890, "payments": {"a": 0, "b": 890, "c": 0, "d": 0}},
               "rent": {"bill": 1200, "payments": {"a": 0, "b": 0, "c": 1200, "d": 000}}
               }
    events = getPaymentExchangeInformation(totalMembers, expense)
    for event in events:
        print(event)
