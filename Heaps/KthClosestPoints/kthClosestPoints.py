import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] 

        for point in points:
                dist = point[0]**2 + point[1]**2
                heap.append((dist, point[0], point[1]))
        heapq.heapify(heap)

        points = []

        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            points.append((x, y))

        return points