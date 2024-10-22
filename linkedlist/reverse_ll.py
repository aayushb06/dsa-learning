"""Reverse a linked list A from position B to C.
NOTE: Do it in-place and in one-pass.

Problem Constraints
    1 <= |A| <= 106
    1 <= B <= C <= |A|

Input Format
    The first argument contains a pointer to the head of the given linked list, A.
    The second arugment contains an integer, B.
    The third argument contains an integer C.

Output Format
    Return a pointer to the head of the modified linked list.

Example Input
Input 1:

 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 2
 C = 4

Input 2:

 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 1
 C = 5


Example Output
Output 1:

 1 -> 4 -> 3 -> 2 -> 5
Output 2:

 5 -> 4 -> 3 -> 2 -> 1


Example Explanation
Explanation 1:

 In the first example, we want to reverse the highlighted part of the given linked list : 1 -> 2 -> 3 -> 4 -> 5 
 Thus, the output is 1 -> 4 -> 3 -> 2 -> 5 
Explanation 2:

 In the second example, we want to reverse the highlighted part of the given linked list : 1 -> 4 -> 3 -> 2 -> 5  
 Thus, the output is 5 -> 4 -> 3 -> 2 -> 1 
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
        
    def reverse_from_target_to_end(self, start, end):
        if not self.head or start==end:
            return None
        temp = Node(0)
        temp.next = self.head
        prev_node = temp
        i=0
        while i < start-1:
           prev_node = prev_node.next
           i+=1
        
        current_node = prev_node.next
        next_node = None
        previous_sublist = prev_node
        remaining_sublist = current_node
        
        for _ in range(end-start+1):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        
        previous_sublist.next.next = current_node
        previous_sublist.next = prev_node
        self.head = temp.next
    
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
    linkedlist.push(7)
    linkedlist.print_ll()
    linkedlist.reverse_from_target_to_end(start=2, end=4)
    linkedlist.print_ll()
