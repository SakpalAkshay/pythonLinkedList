class Node:
    def _init_(self,data):
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


def insertAtIthR(head,position,data):
    if position<0:
        return head
    
    if position==0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    
    if head is None:
        return None
    newHead = insertAtIthR(head.next, position - 1, data)
    head.next = newHead
    return head

printLL(head)
