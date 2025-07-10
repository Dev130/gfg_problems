class Solution:
    def countConsec(self, n: int) -> int:
        dp = [[0, 0] for _ in range(n+1)]
        dp[1][0] = 1
        dp[1][1] = 1
        
        for i in range(2, n+1):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]
        
        valid = dp[n][0] + dp[n][1]
        total = 1 << n  # same as 2^n
        return total - valid
