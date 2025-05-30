class Solution:
    def minChar(self, s):
        #Write your code here
        def computeLPS(pattern):
            lps=[0] * len(pattern)
            length=0
            i=1
            while i<len(pattern):
                if pattern[i]== pattern[length]:
                    length+=1
                    lps[i]=length
                    i+=1
                else:
                    if length !=0:
                        length = lps[length-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
            
        revs=s[::-1]
        combined=s+'#'+revs
        lps= computeLPS(combined)
        return len(s)-lps[-1]
            