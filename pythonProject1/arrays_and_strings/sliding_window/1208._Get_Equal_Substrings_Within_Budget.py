# 1208. Get Equal Substrings Within Budget
# You are given two strings s and t of the same length and an integer maxCost.
#
# You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]|
# (i.e., the absolute difference between the ASCII values of the characters).
#
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring
# of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed
# to its corresponding substring from t, return 0.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = cost = total_cost = answer = 0
        curr = []

        for right in range(len(s)):
            cost = abs(ord(s[right]) - ord(t[right]))
            curr.append(cost)

            total_cost += cost

            while total_cost > maxCost:
                total_cost -= curr[left]
                left += 1

            answer = max(answer, right - left + 1)

        return answer


if __name__ == "__main__":
    solution = Solution()

    # s, t, maxCost = "abcd", "bcdf", 3
    # s, t, maxCost = "abcd", "cdef", 3
    # s, t, maxCost = "abcd", "acde", 0

    s, t, maxCost = "krrgw", "zjxss", 19
    print(solution.equalSubstring(s, t, maxCost))
