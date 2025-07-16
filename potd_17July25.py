class Solution:
    def maxKPower(self, n, k):
        # Helper function to factorize k
        def prime_factors(x):
            factors = {}
            i = 2
            while i * i <= x:
                count = 0
                while x % i == 0:
                    count += 1
                    x //= i
                if count > 0:
                    factors[i] = count
                i += 1
            if x > 1:
                factors[x] = 1
            return factors
        
        # Count exponent of prime p in n!
        def count_p_in_factorial(n, p):
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            return count
        
        # Factorize k
        factors = prime_factors(k)
        
        min_x = float('inf')
        for p, exp in factors.items():
            cnt = count_p_in_factorial(n, p)
            min_x = min(min_x, cnt // exp)
        
        return min_x
