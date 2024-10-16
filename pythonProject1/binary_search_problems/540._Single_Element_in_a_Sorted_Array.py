# 540. Single Element in a Sorted Array
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = last_index = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2

            if mid == 0 and nums[0] != nums[1]:
                return nums[0]

            if mid == last_index and nums[-1] != nums[-2]:
                return nums[-1]

            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            lower_bound = upper_bound = 0
            if nums[mid] == nums[mid - 1]:
                lower_bound = mid - 1
                upper_bound = mid
            elif nums[mid] == nums[mid + 1]:
                lower_bound = mid
                upper_bound = mid + 1

            if (lower_bound - 0) % 2 == 1:
                right = lower_bound - 1

            if (last_index - upper_bound) % 2 == 1:
                left = upper_bound + 1

        return 0


if __name__ == "__main__":
    solution = Solution()

    # nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    nums = [3, 3, 7, 7, 10, 11, 11]
    print(solution.singleNonDuplicate(nums))
