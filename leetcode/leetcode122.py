from typing import List


class Solution122:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(0, len(prices) - 1))
