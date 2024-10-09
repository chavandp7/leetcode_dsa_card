# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = current_sum = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        for element in nums:
            current_sum += element
            answer += prefix_sum[current_sum - k]
            prefix_sum[current_sum] += 1

        return answer


if __name__ == "__main__":
    solution = Solution()

    # nums, k = [1, 1, 1], 2
    # nums, k = [1, 2, 3], 3
    nums, k = [0, 0], 0

    print(solution.subarraySum(nums, k))
