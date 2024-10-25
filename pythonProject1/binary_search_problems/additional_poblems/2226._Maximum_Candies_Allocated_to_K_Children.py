# 2226. Maximum Candies Allocated to K Children
# You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies
# of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.
#
# You are also given an integer k. You should allocate piles of candies to k children such that each child
# gets the same number of candies. Each child can take at most one pile of candies and some piles of candies
# may go unused.
#
# Return the maximum number of candies each child can get.
from typing import List


class Solution:
    def check(self, candies, givenCandies, k):
        children = 0

        for pile in candies:
            children += pile // givenCandies
            if children >= k:
                return True

        return False

    def maximumCandies(self, candies: List[int], k: int) -> int:

        if sum(candies) < k:
            return 0

        left = 1
        right = max(candies)
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if self.check(candies, mid, k):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    # candies, k = [5, 8, 6], 3
    candies, k = [2, 5], 11
    print(solution.maximumCandies(candies, k))
