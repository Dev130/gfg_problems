class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        frq = [0] * 26
        for c in word:
            frq[ord(c) - ord('a')] += 1
        frq = [f for f in frq if f > 0]
        if not frq:
            return 0
        frq.sort(reverse=True)
        ans = float('inf')
        for i in range(len(frq)):
            target = frq[i]
            d = 0
            for j in range(len(frq)):
                if frq[j] > target + k:
                    d += frq[j] - (target + k)
                elif frq[j] < target:
                    d += frq[j]
            ans = min(ans, d)
        return ans