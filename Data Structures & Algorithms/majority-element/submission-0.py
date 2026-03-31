class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numbers = {}
        n = len(nums)
        
        for num in nums:
            numbers[num]= 1 + numbers.get(num, 0)
            if numbers[num]>(n/2):
                return num
