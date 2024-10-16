# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:
#
#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.
#
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows - 1
        r = -1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                r = mid
                break
            elif matrix[mid][cols - 1] < target:
                left = mid + 1
            else:
                right = mid - 1

        if r == -1:
            return False

        left = 0
        right = cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    solution = Solution()

    # matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 14
    matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13

    print(solution.searchMatrix(matrix, target))
