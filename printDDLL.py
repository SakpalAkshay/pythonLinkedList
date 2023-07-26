class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


def doublyLL():

    inputLs = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currEle in inputLs:

        if currEle == -1:
            break

        newNode = Node(currEle)
        if head is None: #means our LL is empty as of Now, this code will run only once
            head = newNode
            tail = newNode
        else:
            newNode.prev = tail
            tail.next = newNode
            tail = newNode  #shifted tail from head to new Node

    return head, tail


def displayListForward(head):

    while head is not None:
        print(str(head.data) + " => ", end="")
        head = head.next
    print("None") #represents the end of LL
    return


def displayListBackward(tail):
    while tail is not None:
        print(str(tail.data)+ " => " , end='')
        tail = tail.prev
    print("None")
    return



head, tail = doublyLL()
displayListForward(head)
displayListBackward(tail)    