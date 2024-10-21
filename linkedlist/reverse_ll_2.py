"""You are given a singly linked list having head node A. You have to reverse the linked list and return the head node of that reversed list.
NOTE: You have to do it in-place and in one-pass.
Problem Constraints
    1 <= Length of linked list <= 105
Value of each node is within the range of a 32-bit integer.

Input Format
    First and only argument is a linked-list node A.
Output Format
    Return a linked-list node denoting the head of the reversed linked list.
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
            
    def reverse(self):
        if not self.head:
            return None
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def print_ll(self):
        current_node = self.head
        result = ''
        while current_node:
            result = result + " "+ str(current_node.value) if result else str(current_node.value)
            current_node = current_node.next
        print(result)
        
if __name__ == '__main__':
    linkedlist2 = LinkedList()
    linkedlist2.push(2)
    linkedlist2.push(3)
    linkedlist2.push(4)
    linkedlist2.push(5)
    linkedlist2.push(6)
    linkedlist2.push(7)
    linkedlist2.print_ll()
    linkedlist2.reverse()
    linkedlist2.print_ll()
