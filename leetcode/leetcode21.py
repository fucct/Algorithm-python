class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        print(f"{self.val} -> ", end="")
        if self.next:
            self.next.print()
        else:
            print()


class Solution21:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        while l1 and l2:
            if l1.val >= l2.val:
                result.append(l2.val)
                l2 = l2.next
            else:
                result.append(l1.val)
                l1 = l1.next
        while l1:
            result.append(l1.val)
            l1 = l1.next
        while l2:
            result.append(l2.val)
            l2 = l2.next

        if not result:
            resultNode = ListNode()
            return resultNode
        num = result.pop()
        resultNode = ListNode(num)
        while result:
            num = result.pop()
            resultNode = ListNode(num, resultNode)
        return resultNode

