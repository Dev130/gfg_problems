class Solution:
    def minSum(self, arr):
        arr.sort()
        num1 = []
        num2 = []

        for i in range(len(arr)):
            if i % 2 == 0:
                num1.append(str(arr[i]))
            else:
                num2.append(str(arr[i]))

        # Helper to perform string-based addition
        def addStrings(n1, n2):
            res = []
            carry = 0
            i, j = len(n1) - 1, len(n2) - 1
            
            while i >= 0 or j >= 0 or carry:
                digit1 = int(n1[i]) if i >= 0 else 0
                digit2 = int(n2[j]) if j >= 0 else 0
                total = digit1 + digit2 + carry
                res.append(str(total % 10))
                carry = total // 10
                i -= 1
                j -= 1

            return ''.join(res[::-1]).lstrip('0') or '0'

        s1 = ''.join(num1)
        s2 = ''.join(num2)
        return addStrings(s1, s2)
