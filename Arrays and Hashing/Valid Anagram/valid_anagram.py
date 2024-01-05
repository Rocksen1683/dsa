from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # making a counter map for both words 
        sCount = Counter(s)
        tCount = Counter(t)

        # they will be anagrams if they have the same count of letters 
        if sCount == tCount:
            return True 

        return False