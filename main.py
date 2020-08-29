from leetcode2 import Solution2
from leetcode21 import ListNode
from leetcode28 import Solution28

sol = Solution2()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
sol.addTwoNumbers(l1, l2).print()
