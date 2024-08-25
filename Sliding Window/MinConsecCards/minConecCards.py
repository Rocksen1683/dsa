class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        #variable sized sliding window 
        #global min => size of window 

        #enumerate; time O(n), space O(n)
        d = defaultdict(int)
        res = float('inf')
        for i, val in enumerate(cards):
            if val in d:
                res = min(res, i - d[val] + 1)
            d[val] = i

        return res if res != float('inf') else -1    