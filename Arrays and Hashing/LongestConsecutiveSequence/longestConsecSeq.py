class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we would need to convert the array to a hashset for O(1) lookup
        #we would need to find the start of the subsequence
        #for that, we would need to check if (n-1) exists in set for a particular n 

        numSet = set(nums) #removes duplicates and gives us O(1) lookup
        longestSeq = 0

        for num in nums:
            if num - 1 not in numSet:
                length = 1 
                # checking how many consecutive numbers are in the set 
                while num + length in numSet:
                    length += 1
                #longest seq will be current max and the length 
                longestSeq = max(longestSeq, length)

        return longestSeq
                

