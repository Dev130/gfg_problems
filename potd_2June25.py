class Solution:
    def countPairs(self, mat1, mat2, x):
        n = len(mat1)
        elements_in_mat2 = set()
        
        # Add all elements from mat2 to the set
        for i in range(n):
            for j in range(n):
                elements_in_mat2.add(mat2[i][j])
        
        count = 0
        
        # Check for each element in mat1 if x - element exists in mat2
        for i in range(n):
            for j in range(n):
                if x - mat1[i][j] in elements_in_mat2:
                    count += 1
                    
        return count
