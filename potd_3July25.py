class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        freq = {}
        max_len = -1
        
        start = 0
        
        for end in range(n):
            # Add current character to freq map
            freq[s[end]] = freq.get(s[end], 0) + 1
            
            # If we have more than k unique characters, shrink window from the left
            while len(freq) > k:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1
                
            # If exactly k unique characters, update max_len
            if len(freq) == k:
                max_len = max(max_len, end - start + 1)
        
        return max_len
