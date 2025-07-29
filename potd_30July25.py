class Solution:
    def cntSubarrays(self, arr, k):
        from collections import defaultdict
        
        count = 0
        curr_sum = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1  # To count the subarrays that start from index 0
        
        for num in arr:
            curr_sum += num
            if (curr_sum - k) in sum_freq:
                count += sum_freq[curr_sum - k]
            sum_freq[curr_sum] += 1
        
        return count
