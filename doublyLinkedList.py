class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None



def takeInput():

    inputLs = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currEle in inputLs:

        if currEle == -1:
            break
        
        newNode = Node(currEle)

        if head is None:
            head = newNode
            tail = newNode
            
        else:
            newNode.prev = tail
            tail.next = newNode
            tail = newNode
    return head, tail


head, tail  = takeInput()



