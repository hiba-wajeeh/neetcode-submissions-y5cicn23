class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCountS = {}
        charCountT = {}

        for c in s:
            if c in charCountS:
                charCountS[c] += 1
            else:
                charCountS[c] = 1
        
        for c in t:
            if c in charCountT:
                charCountT[c] += 1
            else:
                charCountT[c] = 1
        
        if charCountT == charCountS:
            return True
        else:
            return False