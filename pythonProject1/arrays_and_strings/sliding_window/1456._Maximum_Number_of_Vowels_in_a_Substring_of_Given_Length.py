# 1456. Maximum Number of Vowels in a Substring of Given Length
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s
# with length k.
#
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        answer = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        for right in range(min(k, len(s))):
            if s[right] in vowels:
                answer += 1

        left = 0
        curr = answer
        for right in range(k, len(s)):
            if s[right] in vowels:
                curr += 1

            if s[left] in vowels:
                curr -= 1

            left += 1
            answer = max(answer, curr)

        return answer


if __name__ == "__main__":
    solution = Solution()

    # s, k = "abciiidef", 3
    # s, k = "aeiou", 2
    s, k = "leetcode", 3
    print(solution.maxVowels(s, k))
