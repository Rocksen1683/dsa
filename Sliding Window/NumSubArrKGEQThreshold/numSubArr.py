class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #fixed sliding window 
        numArr = 0
        windowAvg = 0
        window = deque(arr[:k])
        windowAvg = sum(window)//k


        for idx, num in enumerate(arr[k:], start = k):
            if windowAvg >= threshold:
                numArr += 1
            
            #move window 
            windowAvg -= window.popleft()//k
            window.append(num)
            windowAvg += num//k
        
        windowAvg = sum(window)//k
        if windowAvg >= threshold:
            numArr += 1

        return numArr