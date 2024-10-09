# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
from collections import defaultdict
from enum import unique


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        indexes = {}
        ans = 1
        last_unique_index = 0
        unique = True

        for right in range(len(s)):
            if s[right] in indexes:
                i = indexes[s[right]]
                ans = max(ans, right - i)
                last_unique_index = i
                unique = False
            elif unique:
                ans = right + 1
            else:
                ans = max(ans, right - last_unique_index)

            indexes[s[right]] = right

        return ans


if __name__ == "__main__":
    solution = Solution()
    # s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"
    s = "abc"

    print(solution.lengthOfLongestSubstring(s))
