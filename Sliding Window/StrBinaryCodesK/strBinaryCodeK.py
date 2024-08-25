class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        #fixed sliding window of length k

        #left bitwise shift => 2^k
        totalCodes = 1 << k
        distinctCodes = set()

        if len(s) < k:
            return False

        l = 0

        for r in range(k, len(s) + 1):
            window = s[l: r]
            
            if window not in distinctCodes:
                distinctCodes.add(window)

            l += 1

        return len(distinctCodes) == totalCodes
        