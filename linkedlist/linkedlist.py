"""Design and implement a Linked List data structure.
A node in a linked list should have the following attributes - an integer value and a pointer to the next node.
It should support the following operations:
insert_node(position, value) - To insert the input value at the given position in the linked list.
delete_node(position) - Delete the value at the given position from the linked list.
print_ll() - Print the entire linked list, such that each element is followed by a single space (no trailing spaces).
Note:
If an input position does not satisfy the constraint, no action is required.
Each print query has to be executed in a new line.

Problem Constraints
    1 <= value <= 105
    1 <= position <= n where, n is the size of the linked-list.

Input Format
    First line contains an integer denoting number of cases, let's say t. Next t line denotes the cases.
Output Format
    When there is a case of print_ll(), Print the entire linked list, such that each element is followed by a single space.
    There should not be any trailing space.

NOTE: You don't need to return anything.

Example Input
Input 1:
5
i 1 23
i 2 24
p
d 1
p

Input 2:
3
i 1 54
d 10
p

Py3 Code structure:


def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer


def delete_node(position):
    # @param position, integer
    # @return an integer


def print_ll():
    # Output each element followed by a space
"""

import sys


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
            
    def insert_node(self, position, value):
        count = 0
        if position == 0 and not self.head:
            self.push(value)
        current_node = self.head
        while current_node and count < position-1:
            current_node = current_node.next
            count +=1
        new_node = Node(value)
        new_node.next = current_node.next
        current_node.next = new_node
    
    def delete_node(self, position):
        if position == 0 and not self.head:
            return
        current_node = self.head
        count = 0
        while current_node.next and count > position-1:
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
        
if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.push(2)
    linkedlist.push(3)
    linkedlist.push(4)
    test_cases = int(input("No of test cases "))
    while test_cases:
        inputs = str(input()).split(' ')
        action = inputs[0]
        if action in ('i', 'insert'):
            if len(inputs)!=3:
                print("position and value is required in input")
                sys.exit(0)
            position = inputs[1]
            value = inputs[2]
            linkedlist.insert_node(int(position), int(value))
        if action in ('d', 'delete'):
            if len(inputs)!=2:
                print("position is required")
                sys.exit(0)
            position = inputs[1]
            linkedlist.delete_node(int(position))
        if action in ('p', 'print'):
            linkedlist.print_ll()
        test_cases-=1
            
            
