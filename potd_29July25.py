class Solution:
    def asciirange(self, s):
        n = len(s)
        first = {}
        last = {}
        
        # Pass 1: Track first and last occurrences
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        # Prefix ASCII sum array
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + ord(s[i])
        
        result = []
        for c in first:
            if first[c] != last[c]:
                l = first[c]
                r = last[c]
                # strictly between => (l+1, r-1), i.e., s[l+1:r]
                ascii_sum = prefix[r] - prefix[l+1]
                if ascii_sum > 0:
                    result.append(ascii_sum)
        return result
