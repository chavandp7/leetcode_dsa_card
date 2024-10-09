# 525. Contiguous Array
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = {0: -1}
        zeroes = ans = 0

        for right in range(len(nums)):
            zeroes += 1 if nums[right] == 0 else -1

            if zeroes in counts:
                ans = max(ans, right - counts[zeroes])
            else:
                counts[zeroes] = right

        return ans


if __name__ == "__main__":
    solution = Solution()

    nums = [0, 1]
    # nums = [0, 1, 0]
    print(solution.findMaxLength(nums))
