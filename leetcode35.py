from typing import List


class Solution35:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        if not nums:
            return 0
        for num in nums:
            if num >= target:
                return idx
            else:
                idx+=1
        return len(nums)