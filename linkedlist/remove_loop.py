"""
You are using Google Maps to help you find your way around a new place. But, you get lost and end up walking in a circle. Google Maps has a way to keep track of where you've been with the help of special sensors.These sensors notice that you're walking in a loop, and now, Google wants to create a new feature to help you figure out exactly where you started going in circles.

Here's how we can describe the challenge in simpler terms: You have a Linked List A that shows each step of your journey, like a chain of events. Some of these steps have accidentally led you back to a place you've already been, making you walk in a loop. The goal is to find out the exact point where you first started walking in this loop, and then you want to break the loop by not going in the circle just before this point.

Problem Constraints
1 <= number of nodes <= 1000

Input Format
The first of the input contains a LinkedList, where the first number is the number of nodes N, and the next N nodes are the node value of the linked list.
The second line of the input contains an integer which denotes the position of node where cycle starts.

Output Format
return the head of the updated linked list.

Example Input
Input 1:
 
1 -> 2
^    |
| - - 
Input 2:

3 -> 2 -> 4 -> 5 -> 6
          ^         |
          |         |    
          - - - - - -


Example Output
Output 1:

 1 -> 2 -> NULL
Output 2:

 3 -> 2 -> 4 -> 5 -> 6 -> NULL

Example Explanation
Explanation 1:

 Chain of 1->2 is broken.
Explanation 2:

 Chain of 4->6 is broken.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

def remove_cycle(head):
    if not head or not head.next:
        return head
    slow_ptr = head
    fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            print("cycle detected")
            break
    else:
        print("no cycle detected")
        return -1
    fast_ptr.next = None


def print_ll(head):
    current_node = head
    result = ''
    while current_node:
        result = result + " "+ str(current_node.value) if result else str(current_node.value)
        current_node = current_node.next
    print(result)


if __name__ == '__main__':
    head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)
    fifth = Node(5)
    head.next = second
    second.next = third
    third.next = forth
    forth.next = fifth
    fifth.next = second
    remove_cycle(head)
    print_ll(head)
    
    head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)
    fifth = Node(5)
    head.next = second
    second.next = third
    third.next = forth
    forth.next = fifth
    remove_cycle(head)
    print_ll(head)
