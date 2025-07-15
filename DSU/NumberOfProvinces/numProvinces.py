class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size 
    
    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX 
        elif self.rank[rootY] < self.rank[rootX]:
            self.root[rootX] = rootY 
        else: 
            self.root[rootY] = rootX 
            self.rank[rootX] += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #use a Union find data structure to check connectivity in O(1)
        n = len(isConnected)
        uf = UnionFind(n)
        numOfComponents = n 

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                    #we found a union
                    numOfComponents -= 1
                    uf.union(i, j)

        return numOfComponents
