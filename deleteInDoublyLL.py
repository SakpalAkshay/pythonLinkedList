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

def deleteIthPosition(head,position):

    if position<0 and position>calculateLinkedListLength(head):
        return head
    
    if position==0:
        head = head.next
        head.prev = None
        return head
    else:
        curr = head
        prev = None
        count = 0
        while count < position:
            prev = curr
            curr = curr.next
            count +=1
        prev.next = curr.next
        curr = curr.next
        if curr is not None:
            curr.prev = prev
    
    return head

newHead = deleteIthPosition(head,3)



def printLinkedList(head): #this head gets passed from the TakeInput function

    while head is not None:
        print(str(head.data) + "=>", end='')
        head = head.next
    print('None')
    return


printLinkedList(newHead)
