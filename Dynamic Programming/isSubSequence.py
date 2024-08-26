class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #two pointers + DP 
        # i => pointer for current chr in s 
        # j => pointer for current chr in t 

        i = 0 
        j = 0 

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                #found in s, move i 
                i += 1
            #not found, move j 
            j += 1
        
        #true if we have traversed through s 
        return i == len(s)