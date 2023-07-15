class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(head):

    while head is not None:
        print(str(head.data)+" => ", end='')
        head = head.next
    print("None")
    return


def takeInput():

    inputLs = [int(ele) for ele in input().split()]
    head = None
    tail = None

    for currEle in inputLs:
        if currEle == -1:
            break

        newNode = Node(currEle)

        if head is None:  # will only for the first iteration to assign head and tail to first node
            head = newNode
            tail = newNode
        else:
            tail.next = newNode  # for creating links and travel through linked list
            tail = newNode

    return head


head = takeInput()
printLL(head)
