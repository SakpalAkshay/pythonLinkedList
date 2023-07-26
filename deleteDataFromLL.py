class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def takeInput():

    inputLS = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currEle in inputLS:
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


def deleteDataLL(head, data):
    if head.data == data:
        head = head.next
        return head

    curr = head.next
    prev = head
    while curr is not None:
        if curr.data == data:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
    return head


def printLinkedList(head):  # this head gets passed from the TakeInput function

    while head is not None:
        print(str(head.data) + "=>", end='')
        head = head.next
    print('None')
    return


printLinkedList(head)
newhead = deleteDataLL(head, 4)
printLinkedList(newhead)
