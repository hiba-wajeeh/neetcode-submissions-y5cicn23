class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequencies = [[] for _ in range(len(nums)+1)]
        res = []

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for num, counts in counts.items():
            frequencies[counts].append(num)
        
        for i in range(len(nums), -1, -1):
            for j in frequencies[i]:
                res.append(j)
                if len(res)==k:
                    return res
        
        return res