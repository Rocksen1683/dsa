class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #backtracking dfs 

        res = []

        def dfs(left, right, s):
            if len(s) == 2*n:
                #valid as every opening has closing
                res.append(s)

            if left < n:
                #can still add opening paranthesis
                dfs(left + 1, right, s + '(')
            
            if right < left:
                #can add closing 
                dfs(left, right + 1, s + ')')

        dfs(0, 0, '')
        return res