# 724. Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the
# sum of all the numbers strictly to the index's right.
#
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
# This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        prefix_sum = []

        for number in nums:
            total_sum += number
            prefix_sum.append(total_sum)

        for i in range(len(nums)):
            left_sum = prefix_sum[i] - nums[i]
            right_sum = total_sum - prefix_sum[i]

            if left_sum == right_sum:
                return i

        return -1


if __name__ == "__main__":
    solution = Solution()

    # nums = [1, 7, 3, 6, 5, 6]
    # nums = [1, 2, 3]
    nums = [2, 1, -1]
    print(solution.pivotIndex(nums))
