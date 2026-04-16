class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.houseRob(nums[1:]), self.houseRob(nums[:-1]))

    def houseRob(self, arr:List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in arr:
            temp = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2