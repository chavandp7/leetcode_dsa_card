# 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value
# and return this value. Any answer with a calculation error less than 10-5 will be accepted.
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        answer = 0
        for i in range(0, k):
            answer += nums[i]
        sum = answer

        for i in range(k, len(nums)):
            sum += nums[i] - nums[i - k]
            answer = max(answer, sum)

        return round(answer / k, 5)


if __name__ == "__main__":
    solution = Solution()
    # nums, k = [1, 12, -5, -6, 50, 3], 4
    nums, k = [5], 1

    print(solution.findMaxAverage(nums, k))
