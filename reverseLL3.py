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

    if head is None or head.next is None:
        return head
    
    sHead = reverse(head.next)
    tail = head.next #we already have tail present of reverse LL through head's next pointer
    tail.next = head
    head.next = None
    return sHead


lss= reverse(ls)
printLinkedList(lss)