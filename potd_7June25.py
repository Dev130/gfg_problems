class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        diff_map = {0: -1}  # diff -> first index where it occurs
        max_len = 0
        sum1 = sum2 = 0
        
        for i in range(n):
            sum1 += a1[i]
            sum2 += a2[i]
            
            curr_diff = sum1 - sum2
            
            if curr_diff in diff_map:
                # If we've seen this difference before, update max_len
                span_length = i - diff_map[curr_diff]
                if span_length > max_len:
                    max_len = span_length
            else:
                # Store first occurrence of this difference
                diff_map[curr_diff] = i
        
        return max_len
