#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0 
        CharSet = set() #Set doesn't accept Duplicated item
        for r in range(len(s)):
            while s[r] in CharSet:
                CharSet.remove(s[l])
                l += 1
            ## if s[r] not in charset
            CharSet.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
# @lc code=end

