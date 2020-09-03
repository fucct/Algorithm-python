class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not (root.left or root.right):
            return 1

        if root.left and not root.right:
            return 1 + self.maxDepth(root.left)
        elif root.right and not root.left:
            return 1 + self.maxDepth(root.right)
        else:
            return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
