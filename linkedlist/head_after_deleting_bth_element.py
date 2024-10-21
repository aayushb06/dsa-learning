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

Example Explanation
Explanation 1:
    In the first example, 4 is the second last element.
Explanation 2:
    In the second example, 1 is the first and the last element.
    1->1->2->3->3


Example Output
    Output 1:
        1->2
    Output 2:
        1->2->3


Example Explanation
    Explanation 1:
        Each element appear only once in 1->2.

Example Input
    Input 1:
        A = 1 -> 2 -> 3 -> 4 -> 5 -> NULL 
    Input 2:
        A = 3 -> NULL 

Example Output
    Output 1:
        5 -> 4 -> 3 -> 2 -> 1 -> NULL 
    Output 2:
        3 -> NULL 

Example Explanation
    Explanation 1:
        The linked list has 5 nodes. After reversing them, the list becomes : 5 -> 4 -> 3 -> 2 -> 1 -> NULL 
    Expalantion 2:
        The linked list consists of only a single node. After reversing it, the list becomes : 3 -> NULL 
"""
