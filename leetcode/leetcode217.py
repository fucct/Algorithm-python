from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for num in nums:
            if num in table:
                return True
            else:
                table[num] = 1
        return False