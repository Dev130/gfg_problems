class Solution:
    def getCount(self, n):
        # Movement map for each digit
        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }

        # Initialize dp table: dp[d][l] = number of sequences of length l starting at digit d
        dp = [[0] * (n + 1) for _ in range(10)]

        # Base case: sequences of length 1
        for d in range(10):
            dp[d][1] = 1

        # Fill dp table for lengths 2 to n
        for l in range(2, n + 1):
            for d in range(10):
                dp[d][l] = sum(dp[nei][l - 1] for nei in moves[d])

        # Total sequences of length n from all digits
        return sum(dp[d][n] for d in range(10))
