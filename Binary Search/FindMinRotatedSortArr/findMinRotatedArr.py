class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        minNumber = 0 

        while left < right:
            mid = (left + right)//2
            if nums[left] < nums[right]:
                return nums[left]
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]