import collections

class Solution:
    def countStrings(self, s: str) -> int:

        n = len(s)

        counts = collections.Counter(s)

   
        distinct_strings_count = n * (n - 1) // 2

        has_duplicate = False

        for char_count in counts.values():
            if char_count > 1:
               
                has_duplicate = True
             
                distinct_strings_count -= char_count * (char_count - 1) // 2

        if has_duplicate:
            distinct_strings_count += 1

        return distinct_strings_count

