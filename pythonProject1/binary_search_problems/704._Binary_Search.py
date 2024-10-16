# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
# to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    # nums, target = [-1, 0, 3, 5, 9, 12], 9
    nums, target = [-1, 0, 3, 5, 9, 12], 2
    print(solution.search(nums, target))
