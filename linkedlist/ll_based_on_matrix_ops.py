"""Given a matrix A of size Nx3 representing operations. Your task is to design the linked list based on these operations.
There are four types of operations:
0 x -1: Add a node of value x before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
1 x -1: Append a node of value x to the last element of the linked list.
2 x index: Add a node of value x before the indexth node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
3 index -1: Delete the indexth node in the linked list, if the index is valid.
A[i][0] represents the type of operation.

A[i][1], A[i][2] represents the corresponding elements with respect to type of operation.

Note: Indexing is 0 based.

Problem Constraints
    1 <= Number of operations <= 1000
    1 <= All node values <= 109

Input Format
    The only argument given is matrix A.

Output Format
    Return the pointer to the starting of the linked list.

Example Input
Input 1:
    A = [   [0, 1, -1]
            [1, 2, -1]
            [2, 3, 1]   ]
Input 2:
    A = [   [0, 1, -1]
            [1, 2, -1]
            [2, 3, 1]
            [0, 4, -1]
            [3, 1, -1]
            [3, 2, -1]  ]


Example Output
Output 1:
    1->3->2->NULL
 
Output 2:
    4->3->NULL

Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: Multi Dimensional Array with Integers, For e.g [[2,3,6,7],[2,3,4,5]]

Python3 Code structure:
========================
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    def solve(self, A):
"""
