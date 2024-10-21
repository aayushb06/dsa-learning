"""Given a linked list of integers, find and return the middle element of the linked list.

NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.

Problem Constraints
    1 <= length of the linked list <= 100000
    1 <= Node value <= 109

Input Format
    The only argument given head pointer of linked list.

Output Format
    Return the middle element of the linked list.

Example Input
Input 1:

 1 -> 2 -> 3 -> 4 -> 5
Input 2:

 1 -> 5 -> 6 -> 2 -> 3 -> 4

Example Output
Output 1:

 3
Output 2:

 2

Example Explanation
Explanation 1:

 The middle element is 3.
Explanation 2:

 The middle element in even length linked list of length N is ((N/2) + 1)th element which is 2.
"""

"""Given a singly linked list, delete middle of the linked list.

For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5

If there are even nodes, then there would be two middle nodes, we need to delete the second middle element.

For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.

Return the head of the linked list after removing the middle node.

If the input linked list has 1 node, then this node should be deleted and a null node should be returned.


Input Format
    The only argument given is the node pointing to the head node of the linked list
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        
    def _get_length(self):
        current_node = self.head
        count = 0
        while current_node:
            count+=1
            current_node = current_node.next
        return count
    
    def find_middle_node(self):
        ll_length = self._get_length()
        mid = ll_length//2
        if not self.head:
            return None
        current_node = self.head
        count = 0
        while current_node.next and count < mid-1:
            current_node = current_node.next
            count+=1
        return current_node.next.value
    
    def print_ll(self):
        current_node = self.head
        result = ''
        while current_node:
            result = result + " "+ str(current_node.value) if result else str(current_node.value)
            current_node = current_node.next
        print(result)
        
if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.push(2)
    linkedlist.push(3)
    linkedlist.push(4)
    linkedlist.push(5)
    linkedlist.push(6)
    linkedlist.print_ll()
    print(linkedlist.find_middle_node())
    
    linkedlist2 = LinkedList()
    linkedlist2.push(2)
    linkedlist2.push(3)
    linkedlist2.push(4)
    linkedlist2.push(5)
    linkedlist2.push(6)
    linkedlist2.push(7)
    linkedlist2.print_ll()
    print(linkedlist2.find_middle_node())
