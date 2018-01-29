## Description: Double linked observer syntex tree
## Author: Pei Zhang

class Observer():
	def __init__(self, left=None, right=None):
		self.left = left
		self.right = right
		self.pre = None
	def setName(name):
		self.name = name

class ATOM(Observer):
	def __init__(self, name):
		super().__init__()
		self.label = 'ATOM'
		self.tag = 0
		self.name = name

class NEG(Observer):
	def __init__(self, left):
		super().__init__(left)
		self.label = 'NEG'		
		self.tag = 1
		self.left.pre = self

class AND(Observer):
	def __init__(self, left, right):
		super().__init__(left, right)		
		self.label = 'AND'
		self.tag = 2
		self.left.pre, self.right.pre = self, self

class GLOBAL(Observer):
	def __init__(self, left, ub, lb=0):
		super().__init__(left)
		self.label = 'GLOBAL'
		self.tag = 3
		self.lb, self.ub = lb, ub
		self.left.pre = self

class UNTIL(Observer):
	def __init__(self, left, right, ub, lb=0):
		super().__init__(left, right)
		self.label = 'UNTIL'
		self.tag = 4
		self.lb, self.ub = lb, ub
		self.left.pre, self.right.pre = self, self