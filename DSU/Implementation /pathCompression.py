class UnionFind: 
	def __init__(self, size):
		self.root = [i for i in range(size)] 
		
	def find(self, x):
		#recursive base case 
		if x == self.root[x]:
			return x 
			
		#do recursion 
		self.root[x] = self.find(self.root[x])
		return self.root[x]
		
	def union(self, x, y):
		#same union as quick union 
		rootX = self.find(x)
		rootY = self.find(y)
		
		if rootX != rootY :
			#update root y 
			self.root[rootY] = rootX 
			
	def connected(self, x, y):
		return self.find(x) == self.find(y)