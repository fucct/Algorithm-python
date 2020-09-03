from math import inf
from typing import List

from leetcode.leetcode100 import TreeNode


class Solution:
    # iterative
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [[root, float(-inf), float(inf)]]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            if lower >= root.val or root.val >= upper:
                return False
            stack.append([root.left, lower, root.val])
            stack.append([root.right, root.val, upper])
        return True

    # recursive
    def recurse(self, root: TreeNode, lower=float(-inf), upper=float(inf)) -> bool:
        if not root:
            return True

        if root.val <= lower or root.val >= upper:
            return False

        return self.recurse(root.left, lower, root.val) and self.recurse(root.right, root.val, upper)
