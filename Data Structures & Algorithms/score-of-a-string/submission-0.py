class Solution:
    def scoreOfString(self, s: str):
        prefix = [0]*len(s)

        for i in range(1, len(s)):
            prefix[i] = abs(ord(s[i]) - ord(s[i-1]))
        
        sum = 0
        for i in range(1, len(prefix)):
            sum = sum+prefix[i]
        
        return sum