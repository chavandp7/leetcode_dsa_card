# Given a string s, reverse the string according to the following rules:
#
#     All the characters that are not English letters remain in the same position.
#     All the English letters (lowercase or uppercase) should be reversed.
#
# Return s after reversing it.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        input = list(s)

        while left < right:
            while left < right and not input[left].isalpha():
                left += 1

            while left < right and not input[right].isalpha():
                right -= 1

            if left < right:
                temp = input[left]
                input[left] = input[right]
                input[right] = temp

            left += 1
            right -= 1

        return "".join(input)


if __name__ == "__main__":
    # s = "ab-cd"
    # s = "a-bC-dEf-ghIj"
    s = "Test1ng-Leet=code-Q!"

    solution = Solution()
    print(solution.reverseOnlyLetters(s))
