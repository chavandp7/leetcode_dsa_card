# 209._Minimum_Size_Subarray_Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target <= 0:
            return 1

        left = sum = 0
        answer = float('infinity')
        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                answer = min(answer, right - left + 1)
                sum -= nums[left]
                left += 1

        return 0 if answer == float('infinity') else answer


if __name__ == "__main__":
    solution = Solution()

    # target, nums = 7, [2, 3, 1, 2, 4, 3]
    target, nums = 4, [1, 4, 4]

    print(solution.minSubArrayLen(target, nums))
