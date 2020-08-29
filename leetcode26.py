from typing import List


class Solution26:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        length = len(nums)
        if length == 0:
            return 0
        while idx != length:
            length = len(nums)
            if nums.count(nums[idx]) > 1:
                del nums[idx]
                idx -= 1
                length -= 1
            idx += 1
        return len(nums)
