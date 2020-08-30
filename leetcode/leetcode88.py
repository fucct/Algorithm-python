from typing import List


class Solution88:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        first = m - 1
        second = n - 1
        if n == 0:
            return
        for idx in range(1, len(nums1) + 1):
            index = idx * -1

            if nums1[first] >= nums2[second]:
                nums1[index] = nums1[first]
                nums1[first] = 0
                first -= 1
            else:
                nums1[index] = nums2[second]
                nums2[second] = 0
                second -= 1
            if first < 0 or second < 0:
                break

        if first >= 0 and idx <= len(nums1):
            for i in range(idx + 1, len(nums1) + 1):
                index = i * -1
                nums1[index] = nums1[first]
                first -= 1

        if second >= 0 and idx <= len(nums1):
            for i in range(idx + 1, len(nums1) + 1):
                index = i * -1
                nums1[index] = nums2[second]
                second -= 1
