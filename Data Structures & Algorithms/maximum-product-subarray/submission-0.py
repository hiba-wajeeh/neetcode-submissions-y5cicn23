class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # cant be zero in case max in nums is negative
        curMin, curMax = 1, 1

        for n in nums:
            if n==0:
                curMin, curMax = 1, 1
                continue
            
            temp = curMax * n
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(temp, n*curMin, n)
            res = max(curMax, res)
        
        return res