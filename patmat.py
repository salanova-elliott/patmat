#Constructs a pattern matching trie and prints list of nodes
from __future__ import print_function
from trienode import TrieNode
import sys

file_object = open(sys.argv[1])
seqs = []
node_num = 2

#Loads seqs
for line in file_object:
	seqs.append(list(line.rstrip()))

#Initializes root node
root = TrieNode("R", 1)

#Trie construction
for seq in seqs:

	#Resets each new seq to start at root node
	current_node = root

	for bp in seq:

		#Checks if node already exists as a child for current node
		if all(child.bp != bp for child in current_node.children):
			new_node = TrieNode(bp, node_num)
			current_node.addChild(new_node)
			current_node = new_node
			node_num += 1

		#If it exists, follows path of existing node
		else:
			for child in current_node.children:
				if child.bp == bp:
					current_node = child

#Recursively prints node info and calls itself on children
def printer(num, node):
	print("{} {} {}".format(num, node.num, node.bp))

	for child in node.children:
		printer(node.num, child)

printer(1, root)

