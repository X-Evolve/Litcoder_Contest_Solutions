
iStack, oStack = [],[]

def enqueue(value):
    iStack.append(value)

def dequeue():
    if len(oStack) == 0 and len(iStack) == 0:
        return -1
    elif len(oStack) == 0 and len(iStack) > 0:
        while len(iStack) > 0:
            oStack.append(iStack.pop())
        return oStack.pop()
    else:
        return oStack.pop()

def get():
    if len(oStack) == 0 and len(iStack) == 0:
        return -1
    elif len(oStack) == 0 and len(iStack) > 0:
        while len(iStack) > 0:
            oStack.append(iStack.pop())
        return oStack[-1]
    else:
        return oStack[-1]

operations = input().split(",")
for operation in operations:
    operator = operation.split(" ")[0]
    if operator == "1":
        enqueue(int(operation.split(" ")[1]))
    elif operator == "2":
        dequeue()
    elif operator == "3":
        print(get())
