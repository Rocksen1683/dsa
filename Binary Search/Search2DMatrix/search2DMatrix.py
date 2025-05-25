from collections import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        top = 0 
        bot = n - 1

        #find the row
        while top <= bot: 
            mid = (top + bot)//2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target: 
                #found the row
                break
            elif matrix[mid][0] < target:
                #move downwards
                top = mid + 1
            else:
                #move upwards 
                bot = mid - 1

        
        #now we have row idx 
        row = (top + bot)//2

        #binary search to find the exact cell in the matrix 
        left = 0 
        right = n - 1

        while left <= right:
            mid = (left + right)//2

            if matrix[row][mid] == target:
                return True 
            elif matrix[row][mid] < target:
                #move rightwards 
                left = mid + 1 
            else: 
                #move leftwards
                right = mid - 1


        return False
