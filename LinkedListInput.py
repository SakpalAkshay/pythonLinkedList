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

headOfLinkedList = takeInput()
        

ls = takeInput()
print(ls)