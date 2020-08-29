from typing import List


class Solution53:
    def maxSubArray(self, nums: List[int]) -> int:
        result = []
        maxSum = 0
        flag = False
        for num in nums:
            if num >= 0:
                flag = True
            result.append(num)
            if sum(result) < 0:
                result = []
                continue
            thisSum = sum(result)
            maxSum = max(maxSum, thisSum)
        if not flag:
            return max(nums)
        return maxSum
