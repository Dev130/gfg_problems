class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcmTriplets(self, n):
        # Base cases for small n
        if n == 1:
            return 1
        if n == 2:
            return 2  # LCM(1, 2, 2) = 2 or LCM(1,1,2)=2
        if n == 3:
            return 6  # LCM(1, 2, 3) = 6

        # Case 1: n is odd
        if n % 2 != 0:
            return n * (n - 1) * (n - 2)
        # Case 2: n is even
        else:
            # Check if n and n-3 are coprime
            if self.gcd(n, n - 3) == 1:
                return n * (n - 1) * (n - 3)
            else:  # n is even, and n, n-3 are not coprime (i.e., gcd(n, n-3) != 1)
                return (n - 1) * (n - 2) * (n - 3)