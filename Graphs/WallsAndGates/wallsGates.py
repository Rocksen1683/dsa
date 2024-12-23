from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # var declaration
        wall = -1
        gate = 0 
        emptyRoom = 2147483647
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        q = deque([])

        m = len(rooms)
        n = len(rooms[0])
        dist = 0

        # adding all gates to queue for BFS to get shortest distance
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == gate:
                    q.append((i, j))


        # bradth first search
        while q:
            cur = len(q)
            dist += 1 

            while cur > 0:
                cur -= 1
                x, y = q.popleft()
                for dx, dy in dirs: 
                    curX = x + dx
                    curY = y + dy

                    if 0 <= curX < m and 0 <= curY < n and rooms[curX][curY] == emptyRoom:
                        rooms[curX][curY] = dist
                        q.append((curX, curY))


        return rooms

