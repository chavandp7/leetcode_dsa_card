# 2208. Minimum Operations to Halve Array Sum
# You are given an array nums of positive integers. In one operation, you can choose any number from nums
# and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)
#
# Return the minimum number of operations to reduce the sum of nums by at least half.
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        curr_sum = total_sum

        nums = [-num for num in nums]
        heapify(nums)

        ops = 0

        while curr_sum > total_sum / 2:
            n = -heappop(nums)
            curr_sum -= n / 2
            heappush(nums, -1 * n / 2)
            ops += 1

        return ops


if __name__ == "__main__":
    solution = Solution()

    # nums = [5, 19, 8, 1]
    nums = [3, 8, 20]
    print(solution.halveArray(nums))
