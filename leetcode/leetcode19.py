from leetcode.leetcode21 import ListNode


class Solution19:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nextNode = head
        previousNode = head

        for i in range(0, n + 1):
            if not nextNode:
                head = head.next
                return head
            nextNode = nextNode.next

        while nextNode:
            nextNode = nextNode.next
            previousNode = previousNode.next
        previousNode.next = previousNode.next.next

        return head
