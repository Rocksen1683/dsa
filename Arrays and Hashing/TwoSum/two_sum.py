class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of two numbers whose sum equals to target

        Analysis:   
        Brute Force Solution - O(n^2)
        Optimal Solution with hashmap - O(n)
        """

        numMap = {}
        
        #using enumerate to get access to the index as well 
        for idx, num in enumerate(nums):
            #checking if we have already encountered difference 
            if target - num in numMap:
                return [numMap[target - num], idx]
            #adding number to hashmap if difference not present
            else:
                numMap[num] = idx 