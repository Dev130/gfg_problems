from collections import Counter
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        freq=Counter(s)
        for ch in s:
            if freq[ch]==1:
                return ch
        
        return -1        
    
    