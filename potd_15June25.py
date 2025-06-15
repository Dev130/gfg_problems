import math

class Solution:
    def smallestDivisor(self, arr, k):
        def compute_sum(divisor):
            return sum((x + divisor - 1) // divisor for x in arr)  # Avoids math.ceil

        left, right = 1, max(arr)
        answer = right

        while left <= right:
            mid = (left + right) // 2
            if compute_sum(mid) <= k:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
