# 1732. Find the Highest Altitude
# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.
#
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points
# i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        result = 0

        for i in range(len(gain)):
            height = altitudes[-1] + gain[i]
            result = max(result, height)
            altitudes.append(height)

        return result


if __name__ == "__main__":
    solution = Solution()

    # gain = [-5, 1, 5, 0, -7]
    gain = [-4, -3, -2, -1, 4, 3, 2]
    print(solution.largestAltitude(gain))
