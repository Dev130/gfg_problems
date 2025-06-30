class Solution:
    def substrCount(self, s, k):
        if k > len(s):
            return 0

        count = 0
        freq = {}
        distinct = 0

        # Initialize the first window
        for i in range(k):
            c = s[i]
            if c not in freq:
                freq[c] = 0
                distinct += 1
            freq[c] += 1

        if distinct == k - 1:
            count += 1

        # Slide the window
        for i in range(k, len(s)):
            left_char = s[i - k]
            right_char = s[i]

            # Remove the left_char
            freq[left_char] -= 1
            if freq[left_char] == 0:
                distinct -= 1
                del freq[left_char]

            # Add the right_char
            if right_char not in freq:
                freq[right_char] = 0
                distinct += 1
            freq[right_char] += 1

            if distinct == k - 1:
                count += 1

        return count
