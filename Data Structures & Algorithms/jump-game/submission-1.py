class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False  # can't reach this position
            farthest = max(farthest, i + nums[i])
        return True