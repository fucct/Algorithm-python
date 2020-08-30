from leetcode.leetcode21 import ListNode


class Solution83:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = []
        while head:
            if not result:
                result.append(head.val)
                head = head.next
                continue
            if not head.val == result[-1]:
                result.append(head.val)
            head = head.next

        if not result:
            return
        resultNode = ListNode(result.pop())
        while result:
            resultNode = ListNode(result.pop(), resultNode)
        return resultNode

