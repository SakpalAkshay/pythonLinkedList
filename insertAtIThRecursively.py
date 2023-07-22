class Node:
    def _init_(self,data):
        self.data = data
        self.next = None



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