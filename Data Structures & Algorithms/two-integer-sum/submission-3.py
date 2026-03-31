class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        i = 0

        for num in nums:
            diff = target-num
            if diff in prev:
                if i<prev[diff]:
                    return [i, prev[diff]]
                else:
                    return [prev[diff], i]
            prev[num] = i
            i = i+1
        
        return []