# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.leetcode100 import TreeNode


class Solution101:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.recursive(root.left, root.right)

    def recursive(self, left: TreeNode, right: TreeNode):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.recursive(left.left, right.right) and self.recursive(left.right, right.left)