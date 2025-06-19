from collections import Counter

class Solution:
    def validgroup(self, arr, k):
        n = len(arr)
        if n % k != 0:
            return False  # Cannot divide into equal groups

        count = Counter(arr)
        for num in sorted(count):
            freq = count[num]
            if freq > 0:
                for i in range(k):
                    if count[num + i] < freq:
                        return False  # Not enough to form a group
                    count[num + i] -= freq
        return True
