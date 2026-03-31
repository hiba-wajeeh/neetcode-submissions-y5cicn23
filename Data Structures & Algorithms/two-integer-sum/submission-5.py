class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        i = 0

        for num in nums:
            diff = target-num

            if diff in diffs:
                return [diffs[diff], i]
            
            diffs[num] = i
            i += 1
        
        return []