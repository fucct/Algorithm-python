from leetcode.leetcode21 import ListNode


class Solution206:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        return self.recurse(head)

    def recurse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.recurse(n, node)
