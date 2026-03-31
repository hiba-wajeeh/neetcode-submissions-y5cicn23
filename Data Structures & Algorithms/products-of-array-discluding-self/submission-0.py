class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        res = [1]*len(nums)

         # prefix[i] = product of nums[0..i-1]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        # postfix[i] = product of nums[i+1..n-1]
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        for i in range(n):
            res[i] = prefix[i] * postfix[i]

        return res