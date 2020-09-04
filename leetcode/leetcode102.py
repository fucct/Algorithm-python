from typing import List

from leetcode.leetcode100 import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        level = [root]
        while level:
            curr = []
            nextLevel = []
            for node in level:
                curr.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            result.append(curr)
            level = nextLevel
        return result

