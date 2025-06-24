from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        freq = Counter(s)
        freq_values = list(freq.values())
        count_freq = Counter(freq_values)

        if len(count_freq) == 1:
            return True  # All characters have the same frequency

        if len(count_freq) == 2:
            f1, f2 = count_freq.keys()
            c1, c2 = count_freq[f1], count_freq[f2]

            # Case 1: One frequency is 1 and occurs once
            if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
                return True

            # Case 2: Frequency difference is 1 and the higher frequency occurs only once
            if abs(f1 - f2) == 1:
                if (f1 > f2 and count_freq[f1] == 1) or (f2 > f1 and count_freq[f2] == 1):
                    return True

        return False
