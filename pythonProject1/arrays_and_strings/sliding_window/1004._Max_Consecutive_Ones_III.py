# 1004. Max Consecutive Ones III
from typing import List


# Given a binary array nums and an integer k, return the maximum number of consecutive 1's
# in the array if you can flip at most k 0's.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = answer = 0
        count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1

            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1

            answer = max(answer, right - left + 1)
        return answer


if __name__ == "__main__":
    # nums, k = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2
    nums, k = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3

    solution = Solution()
    print(solution.longestOnes(nums, k))
