# 1482. Minimum Number of Days to Make m Bouquets
# You are given an integer array bloomDay, an integer m and an integer k.
#
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
#
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used
# in exactly one bouquet.
#
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden.
# If it is impossible to make m bouquets return -1.
from typing import List


class Solution:
    def check(self, bloomDay, day, m, k):
        items = bouquets = 0
        last_index = -1

        for index, d in enumerate(bloomDay):
            if day >= d:
                if index - last_index == 1:
                    items += 1
                    last_index = index
                else:
                    last_index = index
                    items = 1

            if items == k:
                bouquets += 1
                items = 0

            if bouquets >= m:
                return True

        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left = 1
        right = max(bloomDay)
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if self.check(bloomDay, mid, m, k):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    # bloomDay, m, k = [1, 10, 3, 10, 2], 3, 1
    # bloomDay, m, k = [1, 10, 3, 10, 2], 3, 2
    bloomDay, m, k = [7, 7, 7, 7, 12, 7, 7], 2, 3
    print(solution.minDays(bloomDay, m, k))
