#class for Linked List Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


#method to take linked list input and return the head of Linked list
def takeInput():
    #input list that will become a linked list
    inputLs = [int(ele) for ele in input().split()]
    head = None
    tail = None         #tail will help us in tranversing
    for currEle in inputLs:
        if currEle==-1:
            break

        newNode = Node(currEle)

        #if head is none that we need to make the first element as our head
        if head is None:
            head = newNode
            tail = newNode
        else:
            #will work for second element as in the first iteration tail and head are pointing at first element
            tail.next = newNode #will eventually update the head.next but we dont want our head to move
            #now our tail will get updated as to transverse on newly added nodes
            tail = newNode

    return head

#printing our linked list
def printLL(head):

    while head is not None:
        print(str(head.data) + " => ",end='')
        head = head.next
    print("None")
    return

def lenghtLL(head):
    count = 0
    while head is not None:
        count+=1
        head = head.next
    return count

#function to insert at Ith position
def insertAtIth(head,position,data):

    if position<0 or position>lenghtLL(head):
        return head
    
    #will two pointer to maintain details about current and previous whose btw we have to add our new node
    prev = None
    curr = head
    #no we need a counter so that we can tranverse to that ith posiiton
    count = 0
    while count<position:
        prev = curr
        curr = curr.next
        count+=1
    
    newNode = Node(data)
    if prev is not None: #means if are not inserting at 1st element or head
        prev.next = newNode
    else: #means we are first position
        head = newNode
    newNode.next = curr
    return head

head = takeInput()
printLL(head)
head = insertAtIth(head,3,12)
printLL(head)
head = insertAtIth(head,0,9)
printLL(head)
head = insertAtIth(head,lenghtLL(head),96)
printLL(head)







    
