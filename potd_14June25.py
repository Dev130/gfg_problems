class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        # Both nodes are None
        if not left and not right:
            return True
        # Only one is None
        if not left or not right:
            return False
        # The values must be equal, and their subtrees must be mirrors
        return (left.data == right.data and
                self.isMirror(left.left, right.right) and
                self.isMirror(left.right, right.left))
