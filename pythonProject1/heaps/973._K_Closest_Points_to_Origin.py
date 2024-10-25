# 973. K Closest Points to Origin
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
# return the k closest points to the origin (0, 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
#
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
from heapq import heappush, heappop
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for point in points:
            x, y = point
            distance = sqrt(x * x + y * y)
            heappush(pq, (-distance, point))

            if len(pq) > k:
                heappop(pq)

        result = []
        while pq:
            item = heappop(pq)
            result.append(item[1])

        return result


if __name__ == "__main__":
    solution = Solution()

    # points, k = [[1, 3], [-2, 2]], 1
    points, k = [[3, 3], [5, -1], [-2, 4]], 2
    print(solution.kClosest(points, k))
