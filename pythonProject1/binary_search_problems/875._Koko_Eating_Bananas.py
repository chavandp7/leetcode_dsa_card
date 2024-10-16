# 875. Koko Eating Bananas
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
# and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead
# and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.
import math
from typing import List


class Solution:
    def check(self, piles, h, mid):
        total = 0
        for pile in piles:
            total += math.ceil(pile / mid)

        return total <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if self.check(piles, h, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    solution = Solution()

    # piles, h = [3, 6, 7, 11], 8
    # piles, h = [30, 11, 23, 4, 20], 5
    piles, h = [30, 11, 23, 4, 20], 6
    print(solution.minEatingSpeed(piles, h))
