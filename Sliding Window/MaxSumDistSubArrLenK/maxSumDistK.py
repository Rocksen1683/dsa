class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #we have length k for size of subarray => fixed sliding window 

        #max subarray sum => global max sum and window sum
        maxSum = 0
        curSum = 0 
        curSet = set() #keeping a hashset to maintain distinctness of subarray

        l = 0 #left pointer to keep track of start of window

        for r in range(len(nums)):
            while nums[r] in curSet:
                curSum -= nums[l]
                curSet.remove(nums[l])
                l += 1
            curSum += nums[r]
            curSet.add(nums[r])

            #maintaining window size of k 
            if r-l+1 == k:
                maxSum = max(maxSum, curSum)
                curSum -= nums[l]
                curSet.remove(nums[l])
                l += 1

        return maxSum