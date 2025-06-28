from bisect import bisect_right

class Solution:
    def countLessEq(self, a, b):
        b.sort()
        res = []
        for x in a:
            count = bisect_right(b, x)
            res.append(count)
        return res
