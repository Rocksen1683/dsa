class UnionFind: 
    def __init__(self, size):
        self.root = [i for i in range(size)]
        
    def find(self, x):
        """
        Find the root element of x 
        """
        return self.root[x]
    
    def union(self, x, y):
        """
        Populate the root array with the connection (x, y)
        """
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY: 
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX  
    
    def connected(self, x, y):
        """
        Check if x and y are connected 
        """
        return self.find(x) == self.find(y) 
