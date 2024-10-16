# 2300. Successful Pairs of Spells and Potions
# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i]
# represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
#
# You are also given an integer success. A spell and potion pair is considered successful if the product
# of their strengths is at least success.
#
# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful
# pair with the ith spell.
import math
from typing import List


class Solution:
    def binary_search(self, potions: List[int], target):
        left = 0
        right = len(potions) - 1

        while left <= right:
            mid = (left + right) // 2
            if potions[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        size = len(potions)
        potions = sorted(potions)

        for i in range(len(spells)):
            element = success / spells[i]
            index = self.binary_search(potions, element)
            result.append(size - index)
        return result


if __name__ == "__main__":
    solution = Solution()

    # spells, potions, success = [5, 1, 3], [1, 2, 3, 4, 5], 7
    # spells, potions, success = [3, 1, 2], [8, 5, 8], 16
    spells, potions, success = [15, 8, 19], [38, 36, 23], 328
    print(solution.successfulPairs(spells, potions, success))


