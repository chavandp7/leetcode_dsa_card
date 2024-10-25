# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?
from heapq import heappush, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heappush(heap, n)

            if len(heap) > k:
                heappop(heap)

        return heappop(heap)


if __name__ == "__main__":
    solution = Solution()

    # nums, k = [3, 2, 1, 5, 6, 4], 2
    nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    print(solution.findKthLargest(nums, k))
