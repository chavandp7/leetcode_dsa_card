# 2540. Minimum Common Value
from typing import List


# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer
# common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
#
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least
# one occurrence of that integer.

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first = second = 0

        while first < len(nums1) and second < len(nums2):
            if nums1[first] == nums2[second]:
                return nums1[first]

            if nums1[first] < nums2[second]:
                first += 1

            else:
                second += 1

        return -1


if __name__ == "__main__":
    # nums1, nums2 = [1, 2, 3], [2, 4]
    # nums1, nums2 = [1, 2, 3, 6], [2, 3, 4, 5]
    nums1, nums2 = [1, 2, 3], []

    solution = Solution()
    print(solution.getCommon(nums1, nums2))
