# note tree data structure

class Tree():
    def __init__(self, data=None):
        self.data = data
        self.children = [] # should be an array of trees

class BinaryTree():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


# NOTES:        
# non-linear data structure: has multiple branches and paths
# linear data structure: (array, list etc.) can start from first and go on from there
# Depth-First-Search V Breadth-First-Search

def dfs(tree):
    if tree is None:
        return 
    else:
        print(tree.data)
        dfs(tree.left)
        dfs(tree.right)
        
def sum_tree(tree):
    if tree is None:
        return 0
    else: 
        left_sum = sum_tree(tree.left)
        right_sum = sum_tree(tree.right)
        return root.data + left_sum + right_sum