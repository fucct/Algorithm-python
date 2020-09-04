from cmath import inf
from typing import List


class Solution88:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        first = m - 1
        second = n - 1
        index = -1

        while first >= 0 and second >= 0:
            if nums1[first] >= nums2[second]:
                nums1[index] = nums1[first]
                nums1[first] = float(-inf)
                first -= 1
            else:
                nums1[index] = nums2[second]
                second -= 1
            index -= 1

        while second >= 0:
            nums1[index] = nums2[second]
            index -= 1
            second -= 1
