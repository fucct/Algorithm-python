# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leetcode.leetcode21 import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :param n:
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val, node.next = node.next.val, node.next.next
