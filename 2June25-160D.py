#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        citations.sort(reverse=True)
        h=0
        for i,c in enumerate(citations):
            if c>=i+1:
                h=i+1
            else:
                break
        return h    