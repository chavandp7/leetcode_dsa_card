# 2260. Minimum Consecutive Cards to Pick Up
# You are given an integer array cards where cards[i] represents the value of the ith card.
# A pair of cards are matching if the cards have the same value.
#
# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards
# among the picked cards. If it is impossible to have matching cards, return -1.
from collections import defaultdict
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        result = float('infinity')
        left = 0
        counts = defaultdict(int)

        for right in range(len(cards)):
            counts[cards[right]] += 1

            while (right - left + 1) - len(counts) >= 1:
                counts[cards[left]] -= 1
                if counts[cards[left]] == 0:
                    del counts[cards[left]]

                result = min(result, right - left + 1)
                left += 1

        if result == float('infinity'):
            return -1
        return result


if __name__ == "__main__":
    solution = Solution()

    # cards = [3, 4, 2, 3, 4, 7]
    cards = [1, 0, 5, 3]
    print(solution.minimumCardPickup(cards))
