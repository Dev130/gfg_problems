class Solution:
    def countBalanced(self, arr):
        vowels = set("aeiou")
        n = len(arr)
        
        # Helper to count net (vowels - consonants) in given string
        def get_delta(s):
            v = sum(1 for c in s if c in vowels)
            c = len(s) - v
            return v - c

        prefix_sum_freq = {}
        prefix_sum_freq[0] = 1  # There is one "empty" prefix
        prefix_sum = 0
        result = 0
        
        for s in arr:
            delta = get_delta(s)
            prefix_sum += delta
            # If this prefix_sum has been seen k times before, there are k substrings ending here with sum 0
            result += prefix_sum_freq.get(prefix_sum, 0)
            prefix_sum_freq[prefix_sum] = prefix_sum_freq.get(prefix_sum, 0) + 1

        return result
