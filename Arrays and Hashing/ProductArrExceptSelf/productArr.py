class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        prefix = 1 
        postfix = 1

        #iterate forward and calculate product
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        #iterate backward and calculate postfix product
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
