"""
Given a sorted linked list, delete all duplicates such that each element appears only once.

Problem Constraints
    0 <= length of linked list <= 106

Input Format
    First argument is the head pointer of the linked list.

Output Format
    Return the head pointer of the linked list after removing all duplicates.

Example Input
Input 1:

 1->1->2
Input 2:
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
            
    def remove_duplicates(self):
        if not self.head or not self.head.next:
            return
        slow_ptr = self.head
        fast_ptr = self.head.next
        
        while fast_ptr.next:
            
            if slow_ptr.value == fast_ptr.value:
                current_node = fast_ptr
                fast_ptr = fast_ptr.next
                current_node.next = None
                slow_ptr.next = fast_ptr
            else:
                slow_ptr = fast_ptr
                fast_ptr = fast_ptr.next
    
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
    linkedlist2.push(4)
    linkedlist2.push(5)
    linkedlist2.push(6)
    linkedlist2.push(6)
    linkedlist2.push(7)
    linkedlist2.print_ll()
    linkedlist2.remove_duplicates()
    linkedlist2.print_ll()
