# 713. Subarray Product Less Than K
# Given an array of integers nums and an integer k, return the number of contiguous
# subarrays where the product of all the elements in the subarray is strictly less than k.
from itertools import product
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = answer = 0
        product = 1

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k and left <= right:
                product = product / nums[left]
                left += 1

            answer = answer + (right - left + 1)

        return answer


if __name__ == "__main__":
    # nums, k = [10, 5, 2, 6], 100
    # nums, k = [1, 2, 3], 0
    nums, k = [1, 1, 1], 1

    solution = Solution()
    print(solution.numSubarrayProductLessThanK(nums, k))
