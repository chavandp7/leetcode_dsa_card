# 1870. Minimum Speed to Arrive on Time
# You are given a floating-point number hour, representing the amount of time you have to reach the office.
# To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.
# Each train can only depart at an integer hour, so you may need to wait in between each train ride.
#     For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before
#     you can depart on the 2nd train ride at the 2 hour mark.
#
# Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you
# to reach the office on time, or -1 if it is impossible to be on time.
# Tests are generated such that the answer will not exceed 107 and hour will
# have at most two digits after the decimal point.
import math
from typing import List


class Solution:
    def check(self, dist: List[int], speed, hour):
        time = 0
        for i in range(len(dist)):
            time = math.ceil(time)
            time += dist[i] / speed

        return time <= hour

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > math.ceil(hour):
            return -1

        left = 1
        right = 10 ** 7
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if self.check(dist, mid, hour):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    solution = Solution()

    # dist, hour = [1, 3, 2], 6
    # dist, hour = [1, 3, 2], 2.7
    # dist, hour = [1, 3, 2], 1.9
    dist, hour = [1, 1, 100000], 2.01
    print(solution.minSpeedOnTime(dist, hour))
