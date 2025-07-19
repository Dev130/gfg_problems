class Solution:
    def countValid(self, n, arr):
        total_count = 9 * (10**(n - 1))
        
        forbidden_digits = set(arr)
        m = 10 - len(forbidden_digits)
        
        count_bad_numbers = 0
        if 0 not in forbidden_digits:
            count_bad_numbers = (m - 1) * (m**(n - 1))
        else:
            count_bad_numbers = m**n
            
        return total_count - count_bad_numbers