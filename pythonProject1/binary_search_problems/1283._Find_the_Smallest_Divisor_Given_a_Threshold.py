# 1283. Find the Smallest Divisor Given a Threshold
# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor,
# divide all the array by it, and sum the division's result. Find the smallest divisor such that the
# result mentioned above is less than or equal to threshold.
#
# Each result of the division is rounded to the nearest integer greater than or equal to that element.
# (For example: 7/3 = 3 and 10/2 = 5).
#
# The test cases are generated so that there will be an answer.
import math
from typing import List


class Solution:
    def check(self, nums, mid, threshold):
        avg = 0
        for num in nums:
            avg += math.ceil(num / mid)

        return avg <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if self.check(nums, mid, threshold):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    # nums, threshold = [1, 2, 5, 9], 6
    nums, threshold = [44, 22, 33, 11, 1], 5
    print(solution.smallestDivisor(nums, threshold))
