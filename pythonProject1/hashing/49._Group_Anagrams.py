# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import defaultdict
from lib2to3.pgen2.tokenize import group
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)
            anagrams[sorted_word].append(word)

        for key in anagrams.keys():
            result.append(anagrams[key])

        return result


if __name__ == "__main__":
    solution = Solution()

    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs = [""]
    print(solution.groupAnagrams(strs))
