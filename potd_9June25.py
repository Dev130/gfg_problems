class Solution:
    def isDeadEnd(self, root):
        def dfs(node, min_val, max_val):
            if not node:
                return False
            
            # If the allowed range collapses to a single point → Dead End
            if min_val == max_val:
                return True
            
            # Check left and right subtrees
            left_dead_end = dfs(node.left, min_val, node.data - 1)
            right_dead_end = dfs(node.right, node.data + 1, max_val)
            
            return left_dead_end or right_dead_end
        
        # Initial range is [1, ∞] (since node values > 0)
        return dfs(root, 1, float('inf'))
