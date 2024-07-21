from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        time = 0 #global time required 

        maxHeap = [-1*task for task in taskCount.values()]
        heapq.heapify(maxHeap)

        q = deque() #queue to figure out order 

        while maxHeap or q:
            time += 1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
