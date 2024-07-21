import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #use a max heap
        heap = [-1*num for num in nums]

        heapq.heapify(heap)
                
        for i in range(k):
            if i == k-1:
                return -1*heapq.heappop(heap)
            heapq.heappop(heap)
