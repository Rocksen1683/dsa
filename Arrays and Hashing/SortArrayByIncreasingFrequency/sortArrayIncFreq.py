class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numCount = Counter(nums).most_common()
        numCount.sort(key = lambda x: x[0], reverse=True)
        numCount.sort(key = lambda x: x[1])

        res = []
        for val in numCount:
            num, count = val
            res.extend([num]*count)
        
        return res