class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l = 0
        length = 0
        seen = set()

        for r in range(len(s)):
            # shrink from left until duplicate is removed
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            length = max(length, r - l + 1)
        
        return length