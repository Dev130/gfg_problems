'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        res = -1  # Initialize result as -1 (in case no valid node is found)
        
        while root:
            if root.data <= k:
                res = root.data  # This is a possible result
                root = root.right  # Try to find a bigger one ≤ k
            else:
                root = root.left  # Discard this node and go left
        
        return res
