from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print(self):
        print(self.val, end=" ")
        if self.left:
            self.left.print()
        elif self.right:
            print("null", end=" ")
        if self.right:
            self.right.print()


class Solution100:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_list = self.treeToList(p)
        q_list = self.treeToList(q)

        return p_list == q_list

    def treeToList(self, head: TreeNode) -> List[int]:
        result = []
        if head:
            result.append(head.val)
            if head.left:
                result = [*result, *self.treeToList(head.left)]
            elif head.right:
                result = [*result, "null"]
            if head.right:
                result = [*result, *self.treeToList(head.right)]
            return result
        else:
            return []


