from leetcode.leetcode21 import ListNode


class Solution234:
    def isPalindrome(self, head: ListNode) -> bool:
        first = second = head

        while second and second.next:
            second = second.next.next
            first = first.next

        prev = None
        while first:
            curr = first.next
            first.next = prev
            prev = first
            first = curr

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True
