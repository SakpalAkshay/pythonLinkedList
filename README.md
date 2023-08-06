# A repo to record my learning of Linked List in python.

Linked list is a simple data structure in programming, which obviously is used to store data and retrieve it accordingly. To make it easier to imagine, it is more like a dynamic array in which data elements are linked via pointers (i.e. the present record points to its next record and the next one points to the record that comes after it, this goes on until the end of the structure) rather than being tightly packed.

There are two types of linked list:

Single-Linked List: In this, the nodes point to the node immediately after it

Doubly Linked List: In this, the nodes not only reference the node next to it but also the node before it.

# Two pointer Approach in solving problems
In a singly linked list, there’s no easy way to iterate back through the list when you find the end, thus we’ll need to rely on something known as the two-pointer technique. The two-pointer technique allows us to keep two-pointers referencing two different locations in the linked list. If we offset the pointers or increment them at different rates we can solve a lot of interesting problems which we can’t do with just one pointer.
The same approach can be utilized to find the midpoint of the Linked List through one single pass. The first pointer is utilized to hop two elements in one go, while the other hops only one element. 
