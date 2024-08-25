class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #sliding window of size len(p)
        #global arr for start indexes 
        res = []

        if len(p) > len(s):
            return []

        pCount = Counter(p)
        l = 0 
        
        for r in range(len(p), len(s) + 1):
            window = Counter(s[l:r])

            if pCount == window:
                res.append(l)

            l += 1

        return res
