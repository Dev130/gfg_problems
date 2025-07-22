class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Replace numbers <= 0 or > n with (n+1)
        # since answer must be in range [1, n+1]
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n + 1
        
        # Step 2: Use array indices to mark presence of numbers
        # For number x, mark arr[x-1] as negative
        for i in range(n):
            num = abs(arr[i])
            if num <= n:
                arr[num - 1] = -abs(arr[num - 1])
        
        # Step 3: Find first positive number (unmarked index)
        for i in range(n):
            if arr[i] > 0:
                return i + 1
        
        # If all indices are marked, answer is n+1
        return n + 1
