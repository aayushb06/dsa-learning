"""
Given a linked list A, remove the B-th node from the end of the list and return its head.
For example, given linked list: 1->2->3->4->5, and B = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

NOTE: If B is greater than the size of the list, remove the first node of the list.

Try doing it using constant additional space.

Problem Constraints
    1 <= |A| <= 106

Input Format
    The first argument of input contains a pointer to the head of the linked list. The second argument of input contains the integer B.
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
        if not self.head:
            return 0
        current_node = self.head
        count = 0
        while current_node:
            current_node = current_node.next
            count+=1
        return count
    
    def delete_node(self, position):
        if position == 0 and not self.head:
            return
        elif position == 0 and self.head:
            self.head = self.head.next
            return
        current_node = self.head
        count = 0
        while current_node.next and count < position-1:
            current_node = current_node.next
            count+=1
        temp_node = current_node.next
        current_node.next = temp_node.next
        temp_node.next = None
    
    def print_ll(self):
        current_node = self.head
        result = ''
        while current_node:
            result = result + " "+ str(current_node.value) if result else str(current_node.value)
            current_node = current_node.next
        print(result)
        
    def remove_nth_from_end(self, n):
        if not self.head:
            return
        length = self._get_length()
        if n > length:
            self.delete_node(0)
        else:
            target = length-n
            self.delete_node(target)
        
if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.push(2)
    linkedlist.push(3)
    linkedlist.push(4)
    linkedlist.push(5)
    linkedlist.push(6)
    linkedlist.push(7)
    linkedlist.push(8)
    linkedlist.print_ll()
    linkedlist.remove_nth_from_end(8)
    linkedlist.print_ll()
    linkedlist.remove_nth_from_end(2)
    linkedlist.print_ll()
