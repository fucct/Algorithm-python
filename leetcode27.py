from typing import List


class Solution27:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        length = len(nums)
        while idx != length:
            if nums[idx] == val:
                del nums[idx]
                length -= 1
                continue
            idx += 1
        return len(nums)
