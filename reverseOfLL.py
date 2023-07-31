class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def printLinkedList(head): #this head gets passed from the TakeInput function

    while head is not None:
        print(str(head.data) + "=>", end='')
        head = head.next
    print('None')
    return
    
def takeInput():
    head = None
    tail = None

    inputLs = [int(ele) for ele in input().split()]

    for currEle in inputLs:
        if currEle == -1:
            break
    
        newNode = Node(currEle)

        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head


head = takeInput()
printLinkedList(head)

def reverse(head):
    #base case returns last element when reaching it
    if head is None or head.next is None:
        return head

    smallHead = reverse(head.next) #head gets updated for everycall through head.next
    curr = smallHead
    while curr.next is not None:
        curr = curr.next
    curr.next = head #head being first element and this is connecting last element with head after we have reversed it
    head.next = None
    return smallHead

revHead = reverse(head)
printLinkedList(revHead)


