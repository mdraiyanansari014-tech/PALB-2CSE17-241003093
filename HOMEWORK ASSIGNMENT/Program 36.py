# Given an array of strings strs, group the anagrams together. You can return the answer 
# in any order. 
# Example 1: 
# Input: strs = ["eat","tea","tan","ate","nat","bat"] 
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in anagram_map:
                anagram_map[key] = []

            anagram_map[key].append(word)

        return list(anagram_map.values())


obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = obj.groupAnagrams(strs)
print(result)
