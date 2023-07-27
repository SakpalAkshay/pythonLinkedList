class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



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
            tail.next = newNode
            tail = newNode
            if tail.next is None: # will only run for last node to connect it to first Node
                tail.next = head
    return head


def displayCircularLinkedList(head):
    curr = head
    while curr is not None:
        print(str(curr.data)+"=>", end='')
        curr = curr.next
        if curr == head:
            print(str(curr.data))
            break
        
    print("Completed circular LL")
    return

head = takeInput()
displayCircularLinkedList(head)