class Solution:
    def divby13(self, s):
        remainder = 0
        for ch in s:
            remainder = (remainder * 10 + int(ch)) % 13
        return remainder == 0
