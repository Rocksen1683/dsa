class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        """
        Find the root element of x
        """
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        """
        Populate the root array with the connection (x, y)
        """
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        """
        Check if x and y are connected
        """
        return self.find(x) == self.find(y) 
		