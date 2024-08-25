class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #fixed sliding window of length s1 
        #verify whether the count of chars in window is same as count of s1
        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        windowCount = Counter(s2[:len(s1)])
        print(s1Count)

        remChars = len(s2) - len(s1)

        for idx, ch in enumerate(s2[len(s1):], start = len(s1)):
            if windowCount == s1Count:
                return True 

            windowCount[s2[idx]] += 1
            windowCount[s2[idx - len(s1)]] -= 1
            if windowCount[s2[idx - len(s1)]] == 0:
                del windowCount[s2[idx - len(s1)]]

        return windowCount == s1Count