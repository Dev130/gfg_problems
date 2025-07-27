class Solution:
    def setMatrixZeroes(self, mat):
        n, m = len(mat), len(mat[0])
        first_row_zero = any(mat[0][j] == 0 for j in range(m))
        first_col_zero = any(mat[i][0] == 0 for i in range(n))
        
        # Use first row and col to mark zeroes
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0
        
        # Set zeroes excluding first row and column
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        
        # Set first row to zero if needed
        if first_row_zero:
            for j in range(m):
                mat[0][j] = 0
        
        # Set first column to zero if needed
        if first_col_zero:
            for i in range(n):
                mat[i][0] = 0
