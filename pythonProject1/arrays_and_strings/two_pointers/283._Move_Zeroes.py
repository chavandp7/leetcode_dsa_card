# 283. Move Zeroes
from typing import List


# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of
# the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        size = len(nums)

        while right < size:
            if nums[right] != 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

                left += 1
            right += 1

        # print(nums)


if __name__ == "__main__":
    nums = [1, 0]
    solution = Solution()
    print(solution.moveZeroes(nums))
