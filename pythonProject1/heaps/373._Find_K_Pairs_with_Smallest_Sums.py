# 373. Find K Pairs with Smallest Sums
# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
#
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
#
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
from heapq import heappush, heapify, heappop
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []

        for a in nums1:
            for b in nums2:
                heappush(pq, (-(a + b), [a, b]))
                if len(pq) > k:
                    heappop(pq)

        pq = sorted(pq, reverse=True)

        result = []
        for item in pq:
            result.append(item[1])

        return result


if __name__ == "__main__":
    solution = Solution()
    nums1, nums2, k = [1, 7, 11], [2, 4, 6], 3
    # nums1, nums2, k = [1, 1, 2], [1, 2, 3], 2
    print(solution.kSmallestPairs(nums1, nums2, k))
