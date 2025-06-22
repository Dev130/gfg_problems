class Solution:
    def largestSubset(self, arr):
        if not arr:
            return []

        # Sort in descending order for lexicographically greatest result
        arr.sort(reverse=True)
        n = len(arr)

        dp = [1] * n
        prev = [-1] * n
        max_len = 1
        max_index = 0

        for i in range(n):
            for j in range(i):
                if arr[j] % arr[i] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_len or (dp[i] == max_len and arr[i] > arr[max_index]):
                max_len = dp[i]
                max_index = i

        # Reconstruct result
        result = []
        while max_index != -1:
            result.append(arr[max_index])
            max_index = prev[max_index]

        return sorted(result)  # Sort final result in ascending order as required
