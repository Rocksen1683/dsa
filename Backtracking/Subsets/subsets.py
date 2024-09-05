class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking solution to find all the possible subsets
        """

        res = []

        subset = []
        def dfs(n):
            if n >= len(nums):
                res.append(subset.copy()) #include copy as we are modifying subset
                return

            #to include nums[i]
            subset.append(nums[n])
            dfs(n + 1)

            #to not include nums[i]
            subset.pop()
            dfs(n+1)

        dfs(0)
        return res


