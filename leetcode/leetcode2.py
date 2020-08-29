from leetcode.leetcode21 import ListNode


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        adder = 0
        while l1 and l2:
            num = l1.val + l2.val + adder
            if num >= 10:
                result.append(num-10)
                adder = 1
            else:
                result.append(num)
                adder = 0
            l1 = l1.next
            l2 = l2.next
        while l1:
            num = l1.val + adder
            if num >= 10:
                result.append(num - 10)
                adder = 1
            else:
                result.append(num)
                adder = 0
            l1 = l1.next
        while l2:
            num = l2.val + adder
            if num >= 10:
                result.append(num - 10)
                adder = 1
            else:
                result.append(num)
                adder = 0
            l2 = l2.next
        if adder == 1:
            result.append(adder)

        if not result:
            resultNode = ListNode()
            return resultNode
        num = result.pop()
        resultNode = ListNode(num)
        while result:
            num = result.pop()
            resultNode = ListNode(num, resultNode)
        return resultNode
