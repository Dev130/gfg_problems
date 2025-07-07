from collections import Counter

class Solution:
    def findGreater(self, arr):
        n = len(arr)
        freq = Counter(arr)
        res = [-1] * n
        stack = []
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Pop elements whose frequency is <= current's frequency
            while stack and freq[stack[-1]] <= freq[arr[i]]:
                stack.pop()
            # If stack not empty, top is next element with higher frequency
            if stack:
                res[i] = stack[-1]
            # Push current element to stack
            stack.append(arr[i])
        
        return res
