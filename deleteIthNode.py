class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def calculateLinkedListLength(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def takeInput():

    inputLs = [int(ele) for ele in input().split()]
    head= None
    tail = None
    for curEle in inputLs:

        if curEle == -1:
            break

        newNode = Node(curEle)

        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def printLinkedList(head): #this head gets passed from the TakeInput function

    while head is not None:
        print(str(head.data) + "=>", end='')
        head = head.next
    print('None')
    return


head = takeInput()
printLinkedList(head)
def deleteIthNode(head,position):
    
    if (position<0 or position> calculateLinkedListLength(head)):
        return head


    if position==0:
        head = head.next
        return head
    
    else:
        count = 0
        prev = None
        curr = head
        while count<position:
            prev = curr
            curr = curr.next
            count+=1
        prev.next = curr.next
        del curr
    return head


newHead = deleteIthNode(head,3)
printLinkedList(newHead)