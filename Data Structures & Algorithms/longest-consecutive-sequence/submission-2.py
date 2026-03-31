class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        longest = 0

        for num in nums:
            #check if this is the start of a sequence
            if (num-1) not in all_nums:
                length = 0
                while (num+length) in all_nums:
                    length += 1
                longest = max(length, longest)
        
        return longest