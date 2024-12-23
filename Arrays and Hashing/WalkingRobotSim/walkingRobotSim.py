class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ## need to check if current position is an obstacle, in which we terminate command -> make hashset of obstacles for O(1) lookup 
        ## need to track all position we visited for distance calc 
        ## need to know which direction we're going -> have an array saying which direction 
        ## have a global var for robot position 

        obstacleSet = {(obstacle[0],obstacle[1]) for obstacle in obstacles}
        
        maxDist = 0 
        x, y = 0, 0 

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curDir = 0 

        for command in commands: 
            if command == -1:
                # move right
                curDir = (curDir + 1) % 4
                continue
            elif command == -2: 
                # move left 
                curDir = (curDir + 3) % 4
                continue
            else:
                # move 
                dx, dy = dirs[curDir]
                for _ in range(command):
                    nextX, nextY = x + dx, y + dy 
                    if (nextX, nextY) in obstacleSet:
                        break
                    # update current pos
                    x, y = nextX, nextY

                maxDist = max(maxDist, x**2 + y**2)

        return maxDist
