class TrieNode:

	def __init__(self, bp, num):
		self.bp = bp
		self.num = num

		self.children = []

	def addChild(self, child):
		self.children.append(child)