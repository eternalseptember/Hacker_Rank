"""
You are given pointer to the root of the binary search tree
and two values v1 and v2. You need to return the lowest common
ancestor (LCA) of v1 and v2 in the binary search tree.

At the time of this commit, this problem was not available
for submission in python.
"""


class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None):
		self.data = data
		self.left = left_node
		self.right = right_node

	def __str__(self):
		return str(self.data)


def lowest_common_ancestor(root, val1, val2):
	smaller_value = None
	greater_value = None

	if val1 > val2:
		smaller_value = val2
		greater_value = val1
	else:
		smaller_value = val1
		greater_value = val2

	if (root.data < smaller_value) and (root.data < greater_value):
		return lowest_common_ancestor(root.right, val1, val2)
	elif (root.data > smaller_value) and (root.data > greater_value):
		return lowest_common_ancestor(root.left, val1, val2)
	elif (root.data >= smaller_value) and (root.data <= greater_value):
		return root




# Binary Tree Setup
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)
node6 = Node(6)
node7 = Node(7, node6)
node4 = Node(4, node2, node7)

v1 = 1
v2 = 7

lca = lowest_common_ancestor(node4, v1, v2)
# should be 4
print(lca)

