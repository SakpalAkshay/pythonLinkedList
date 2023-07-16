class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def calculateLinkedListLength(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


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
linkedListLength = calculateLinkedListLength(head)
print(linkedListLength)
