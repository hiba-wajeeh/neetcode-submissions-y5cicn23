class Solution:
    def validPalindrome(self, s: str) -> bool:
        right = len(s)-1
        left = 0

        while left<right:
            if s[left]!=s[right]:
                skipL, skipR = s[left+1:right+1], s[left:right]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            left += 1
            right -= 1
        
        return True