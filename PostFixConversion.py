from stack import myStack

def postFixConverter(expression):

    operators = ['+','*','-','/','(',')']
    operands = ['a','b','c','d']
    operatorsStack = myStack()
    operandsStack = myStack()
    postFixString = ""
    for i in expression:
        if i in operators:
            operatorsStack.push(i)
        else:
            operandsStack.push(i)
            if(len(operandsStack.myList) == 2):
                postFixString = postFixString + operandsStack.myList[0] + operandsStack.myList[1] + operatorsStack.myList[0]
                operandsStack.empty()

    print(operatorsStack.display())
    print(operandsStack.display())

    #operandsStack.empty()
    print(operandsStack.myList)
    print(operatorsStack.getLastElement())
    print(postFixString)

postFixConverter("(d*e)+a")