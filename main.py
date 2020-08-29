from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        for num in nums:
            last = target - num
            try:
                firstNumIdx = nums.index(num)
                lastNumIdx = nums[firstNumIdx + 1:].index(last) + firstNumIdx + 1
                return [firstNumIdx, lastNumIdx]
            except:
                continue
