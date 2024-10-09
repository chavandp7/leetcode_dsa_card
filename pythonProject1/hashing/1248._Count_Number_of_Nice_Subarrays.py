# 1248. Count Number of Nice Subarrays
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are
# k odd numbers on it.
# Return the number of nice sub-arrays.
from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr = answer = 0
        counts = defaultdict(int)
        counts[0] = 1

        for item in nums:
            curr += item % 2
            answer += counts[curr - k]
            counts[curr] += 1

        print(counts)

        return answer


if __name__ == "__main__":
    solution = Solution()

    # nums, k = [1, 1, 2, 1, 1], 3
    # nums, k = [2, 4, 6], 1
    nums, k = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2

    print(solution.numberOfSubarrays(nums, k))
