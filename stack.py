class myStack:
    myList = []

    def display(self):
        return self.myList
        
    def push(self,value):
        self.myList.append(value)
        return self.myList
        
    def pop(self):
        self.myList.pop()
        return self.myList
        
        
 
times = int(input("Enter times"))
for i in range(times):
    obj = myStack()
    size = int(input("Enter size"))
    for j in range(size):
        obj.push(int(input("Enter element")))
    for k in range(size,0,-1):
        print(obj.myList[k - 1])
        obj.pop()
        print(obj.myList)
        

        