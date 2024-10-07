# 557. Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a sentence while still
# preserving whitespace and initial word order.

class Solution:
    def reverse_word(self, s: str) -> str:
        characters = list(s)
        left = 0
        right = len(characters) - 1

        while left < right:
            temp = characters[left]
            characters[left] = characters[right]
            characters[right] = temp
            left += 1
            right -= 1

        return "".join(characters)

    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        result = []

        for i in range(len(words)):
            reversed_word = self.reverse_word(words[i])
            result.append(reversed_word)

        return " ".join(result)


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    # s = "Mr Ding"

    solution = Solution()
    print(solution.reverseWords(s))
