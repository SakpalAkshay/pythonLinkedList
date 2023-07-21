class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



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

head = takeInput()


def printIthNode(head,position):
    # we will traverse the LL and print Node at that position or None if the ith Node doesnt exist

    count = 0 
    curr = head
    while(count<position and curr!=None):
        curr = curr.next
        count+=1
    if curr is None:
        print("No Node exist at given position")
    else:
        print(curr.data, curr)
printIthNode(head,2)