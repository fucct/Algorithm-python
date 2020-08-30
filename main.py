from leetcode.leetcode100 import Solution100, TreeNode
from leetcode.leetcode21 import ListNode
from leetcode.leetcode35 import Solution35
from leetcode.leetcode53 import Solution53
from leetcode.leetcode58 import Solution58
from leetcode.leetcode66 import Solution66
from leetcode.leetcode67 import Solution67
from leetcode.leetcode69 import Solution69
from leetcode.leetcode70 import Solution70
from leetcode.leetcode83 import Solution83
from leetcode.leetcode88 import Solution88

t1 = TreeNode(1, None, TreeNode(3))
t2 = TreeNode(1, TreeNode(2), TreeNode(3))

sol = Solution100()
sol.isSameTree(t1, t2)
