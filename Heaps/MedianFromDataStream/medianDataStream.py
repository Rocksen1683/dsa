import heapq

class MedianFinder:

    def __init__(self):
        #use maxHeap for bottom half elements
        #use minHeap for top half elements
        self.minHeap = []        
        self.maxHeap = []


    def addNum(self, num: int) -> None:
        #first add number to max heap 
        heapq.heappush(self.maxHeap, -1*num)
        #might be possible that pushed element is actually part of maxHeap
        heapq.heappush(self.minHeap, -1*heapq.heappop(self.maxHeap))

        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        #now both heaps are balanced :)

    def findMedian(self) -> float:
        #if length of both heaps are same, return mean of both
        if len(self.maxHeap) == len(self.minHeap):
            return (-1*self.maxHeap[0] + self.minHeap[0])/2
        #otherwise maxHeap will have extra element because of balancing
        return -1*self.maxHeap[0]