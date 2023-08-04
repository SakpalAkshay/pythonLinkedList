class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 


'''If we are able to get head of a Linked list then we can tranverse it very easily'''

def takeInput():

    inputLs = [int(ele) for ele in input().split()] 
    head = None
    
    for currEle in inputLs:
        if currEle == -1:
            break

        newNode = Node(currEle)
        if head is None: 
            head = newNode 
        else:
            curr = head

            while curr.next is not None:
                curr = curr.next 
            curr.next = newNode 
    return head


        
def printLinkedList(head): 

    while head is not None:
        print(str(head.data) + "=>", end='')
        head = head.next
    print('None')
    return
ls = takeInput()
printLinkedList(ls)

def reverse(head):

    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head

lss= reverse(ls)
printLinkedList(lss)