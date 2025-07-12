class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Sorting approach is too slow. Better way is to use Two pointers. Negative pointer moves left to right. Positive pointer moves right to left and negative moves left to right. We have to populate res array in descending order (right to left) as our higher nums will be in the extremes of the array. 
        """
        n = len(nums)
        left = 0 
        right = n - 1 
        res = [0]*n

        for i in range(n-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left]
                left += 1
            else:
                square = nums[right]
                right -= 1

            res[i] = square * square

        return resC

