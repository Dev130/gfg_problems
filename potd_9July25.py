class Solution:
    def sumSubMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)

        # Monotonic stack for Previous Less Element
        stack = []
        prev = [ -1 ] * n
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Monotonic stack for Next Less Element
        stack = []
        next_ = [ n ] * n
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Sum contributions
        res = 0
        for i in range(n):
            left = i - prev[i]
            right = next_[i] - i
            res = (res + arr[i] * left * right) % MOD
        
        return res
