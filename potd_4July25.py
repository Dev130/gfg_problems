from collections import defaultdict

class Solution:
    def countAtMostK(self, arr, k):
        left = 0
        freq = defaultdict(int)
        result = 0
        distinct_count = 0

        for right in range(len(arr)):
            if freq[arr[right]] == 0:
                distinct_count += 1
            freq[arr[right]] += 1

            while distinct_count > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    distinct_count -= 1
                left += 1

            result += (right - left + 1)

        return result
