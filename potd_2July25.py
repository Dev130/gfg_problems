class Solution:
    def totalElements(self, arr):
        from collections import defaultdict
        
        n = len(arr)
        left = 0
        max_len = 0
        count = defaultdict(int)
        
        for right in range(n):
            count[arr[right]] += 1
            
            while len(count) > 2:
                count[arr[left]] -= 1
                if count[arr[left]] == 0:
                    del count[arr[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
