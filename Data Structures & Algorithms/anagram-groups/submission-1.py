class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping character count of each string mapped to list of anagrams

        for s in strs:
            count = [0] * 26 #one 0 for each character 

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s) #tuple bc lists cant be keys in python
        
        return list(res.values())