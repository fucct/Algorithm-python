from typing import List


class Solution189:
    def rotate(self, nums: List[int], k: int) -> None:
        idx = 0
        length = len(nums)
        while idx < (length - k) % length:
            temp = nums[0]
            del nums[0]
            nums.append(temp)
            idx += 1
