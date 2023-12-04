from typing import List

class Solution:
    def check(self, weights, limit, days):
        day = 1
        load = 0
        for i in range(len(weights)):
            if load + weights[i] <= limit:
                load += weights[i]
            else:
                day += 1
                load = weights[i]
        return day <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        ans = high  # Initialize ans to the maximum possible value

        while low <= high:
            mid = (low + high) // 2
            if self.check(weights, mid, days):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
