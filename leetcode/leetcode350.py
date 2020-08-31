from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        result = []
        for num in nums1:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1

        for num in nums2:
            if num in table:
                if table[num] > 0:
                    result.append(num)
                    table[num] -= 1
        return result
