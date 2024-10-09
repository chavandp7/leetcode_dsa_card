# 1189. Maximum Number of Balloons
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon"
# as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)

        for c in text:
            counter[c] += 1

        balloon = ['b', 'a', 'l', 'l', 'o', 'o', 'n']
        answer = float('infinity')

        counter['l'] //= 2
        counter['o'] //= 2

        for c in balloon:
            answer = min(answer, counter[c])

        return answer
