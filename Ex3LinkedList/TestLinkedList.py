class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printVal = self.head

        while printVal is not None:
            print(printVal.val)
            printVal = printVal.next

#myList = LinkedList(0)

bExit = False
i = 0
while not bExit:
    print("Enter a number")
    num = input()
    link1 = Node(num)
    link1.next = link1   
    i+=1
    if i>10:
        bExit = True
        
#Printing Value from list

while (True):
    print(link1.val)
    if link1.next is None:
        break
    link1 = link1.next



    