"""
Try solving it using constant additional space.

Constraints:

0 <= size of linked list <= 106
1 <= value of nodes <= 109

Example:

Input: 
                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 



Expected Output
Enter your input as per the following guideline:
There are 2 lines in the input

Line 1 ( Corresponds to arg 1 ) : Elements in the linked list. First number S is the number of nodes. Then S numbers follow indicating the val in each of the nodes in sequence
	For example, LinkedList: "5 --> 9 --> 7" will be written as "3 5 9 7"(without quotes).

Line 2 : Integer X corresponding to a node position. If the integer is -1, then there is no loop. Otherwise, the end node has a next edge to node number X.
	For example, Integer: "-1" will be written as "-1"(without quotes).
"""

# Floyd's Cycle Detection Algorithm (also known as the Tortoise and Hare algorithm)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_cycle(head):
    if not head and head.next:
        return None
    slow_ptr = head
    fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            break
    else:
        return -1
    slow_ptr = head
    while slow_ptr != fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    return slow_ptr.value


if __name__ == '__main__':
    head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    head.next = second
    second.next = third
    third.next = forth
    forth.next = fifth
    fifth.next = sixth
    sixth.next = third
    print(find_cycle(head))
