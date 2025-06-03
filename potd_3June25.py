class Solution:
    def countSubstr(self, s, k):
        def atMostKDistinct(s, k):
            from collections import defaultdict
            count = defaultdict(int)
            left = 0
            result = 0
            for right in range(len(s)):
                count[s[right]] += 1
                while len(count) > k:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        del count[s[left]]
                    left += 1
                result += right - left + 1
            return result

        # Edge case: if k is 0, no substring is valid
        if k == 0:
            return 0

        return atMostKDistinct(s, k) - atMostKDistinct(s, k - 1)
