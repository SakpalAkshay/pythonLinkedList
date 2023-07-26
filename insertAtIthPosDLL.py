from turtle import position


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

def calculateLinkedListLength(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def insertAtIthPosition(head,position,data):
    if position<0 or position>calculateLinkedListLength(head):
        return None

    curr = head
    prev = None   
    count = 0
    while count < position:
        prev = curr
        curr = curr.next
        count+=1
    
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
        newNode.prev = prev
    else:
        head = newNode
    newNode.next = curr
    if curr is not None:
        curr.prev = newNode
    return head

def displayListForward(head):

    while head is not None:
        print(str(head.data) + " => ", end="")
        head = head.next
    print("None") #represents the end of LL
    return

newHead = insertAtIthPosition(head,5,111)

displayListForward(newHead)