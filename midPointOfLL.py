class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #pointer to the next node


'''If we are able to get head of a Linked list then we can tranverse it very easily'''

def takeInput():

    inputLs = [int(ele) for ele in input().split()] #returns a list
    head = None
    #our break point is -1, if we encounter -1 that means element before that is the last element of linked list
    for currEle in inputLs:
        if currEle == -1:
            break

        newNode = Node(currEle)
        if head is None: #will only get set in the first run of the loop
            head = newNode #once our head is updated we need to create connections in linked lists
        else:
            curr = head

            while curr.next is not None:
                curr = curr.next #this will update the current to last connected node
            curr.next = newNode #will help in connecting the latest additon to linked list
    return head


        

ls = takeInput()
print(ls)



def midPoint(head):
    slow = head
    fast = head
    '''So the find midpoint we divide by 2, here to get done one single pass we are jumping the linked list by 2 elements through fast.next.next
    and making slow jump 1 element through slow.next.
    A LL with 5 elements will have 3 has its midpoint and so does with 6 elements which is element at Index 2'''
    while fast.next !=None and fast.next.next !=None:
        slow = slow.next
        fast = fast.next.next
    
    return slow


MidPoint = midPoint(ls)
print(MidPoint.data, MidPoint)

