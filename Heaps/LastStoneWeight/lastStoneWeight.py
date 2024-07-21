import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #use a max heap to maintain top 2 weights 
        heap = [-1*stone for stone in stones]

        heapq.heapify(heap)
        
        while len(heap) >= 2:
            maxStone = heapq.heappop(heap)
            secStone = heapq.heappop(heap)

            if maxStone != secStone:
                heapq.heappush(heap, -1*abs(maxStone - secStone))

        if heap:
            return -1*heapq.heappop(heap)
        #no stones left
        return 0

        
