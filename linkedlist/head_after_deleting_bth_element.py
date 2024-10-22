"""Example Input
Input 1:
    A = 1->2->3->4->5
    B = 2
Input 2:
    A = 1
    B = 1

Example Output
Output 1:
    1->2->3->5
Output 2:
    None

Example Explanation
Explanation 1:
    In the first example, 4 is the second last element.
Explanation 2:
    In the second example, 1 is the first and the last element.
    1->1->2->3->3
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

    def delete_from_last(self, position):
        if not self.head:
            return None
        temp = Node(0)
        temp.next = self.head
        slow_ptr = temp
        fast_ptr = temp
        
        for _ in range(position):
                fast_ptr = fast_ptr.next
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        slow_ptr.next = slow_ptr.next.next
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
    linkedlist.delete_from_last(2)
    linkedlist.print_ll()

