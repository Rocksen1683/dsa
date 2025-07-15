class UnionFind:
	def __init__(self, size):
		self.root = [i for i in range(size)]
		self.rank = [1] * size
		
	def find(self, x):
		while x != self.root[x]:
			x = self.root[x]
			
		return x 
		
	def union(self, x, y):
		rootX = self.union(x)
		rootY = self.union(y)
		
		if rootX != rootY:
			if self.rank[rootX] > self.rank[rootY]:
				#update root of y as it is smaller
				self.root[rootY] = rootX 
			elif self.rank[rootX] < self.rank[rootY]:
				#update root of x as it is smaller 
				self.root[rootX] = rootY
			else:
				#update whichever but increment new parent with rank + 1
				self.root[rootY] = rootX
				self.rank[rootX] += 1 
				
	def connected(x, y):
		return self.find(x) == self.find(y)
				