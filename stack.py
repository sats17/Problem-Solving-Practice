def findPrecendence(operator):
    if(operator == '+' or operator == '-'):
        return 1
    elif(operator == '*'):
        return 2
    elif(operator == '/'):
        return 3
    else:
        return -1
        
class myStack:
    
    def __init__(self):
        self.myList = []
    
    def display(self):
        return self.myList
        
    def push(self,value):
        self.myList.append(value)
        return self.myList
        
    def pop(self):
        self.myList.pop()
        return self.myList
    
    def isEmpty(self):
        if(len(self.myList) == 0):
            return True
        else:
            return False
    
    def peek(self):
        return self.myList[len(self.myList) - 1]

def infixToPostFix(expression):
    operators = ['+','-','*','/','(',',)']
    conversion = ""
    stack = myStack()
    print(stack.myList)
    for i in expression:
        if i not in operators:
            conversion = conversion + i
        elif(i == '('):
            print("is this working")
            stack.push(i)
        elif(i == ')'):
            print("is this working")
            while(stack.peek() != '('):
                conversion = conversion + stack.peek()
                print("after ) conversion is ",conversion," for i ",i)
                stack.pop()
            stack.pop()    
        else:
            if(not stack.isEmpty() and findPrecendence(i) < findPrecendence(stack.peek())):
                while(not stack.isEmpty()):
                    if(stack.peek == "("):
                        return "Invalid expression"
                    conversion = conversion + stack.peek()
                    stack.pop()
                stack.push(i)
            else:    
                stack.push(i)    
    
    while(not stack.isEmpty()):
        if(stack.peek == '('):
            return "Invalid expression"
        conversion = conversion + stack.peek()
        stack.pop()
            
    
    return conversion
    
print(infixToPostFix("a*(b+c)"))  
# print(findPrecendence('*'))
