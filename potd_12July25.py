class Solution:
    def maxGold(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n = len(mat)
        m = len(mat[0])
        
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        # Fill last column with base values
        for i in range(n):
            dp[i][m-1] = mat[i][m-1]
        
        # Fill the table from second-last column to first
        for j in range(m-2, -1, -1):
            for i in range(n):
                # Initialize max_gold to 0
                max_gold = 0
                
                # Right
                max_gold = max(max_gold, dp[i][j+1])
                
                # Right-up
                if i > 0:
                    max_gold = max(max_gold, dp[i-1][j+1])
                
                # Right-down
                if i < n-1:
                    max_gold = max(max_gold, dp[i+1][j+1])
                
                dp[i][j] = mat[i][j] + max_gold
        
        # Find the maximum in the first column
        return max(dp[i][0] for i in range(n))
