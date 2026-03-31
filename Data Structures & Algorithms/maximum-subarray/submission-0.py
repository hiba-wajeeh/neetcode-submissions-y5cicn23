class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        window_sum = nums[0]
        for i in range(1, len(nums)):
            window_sum = max(nums[i], window_sum+nums[i])  
            max_sum = max(max_sum, window_sum)
        return max_sum