class Solution:
    def caseSort(self, s):
        # Separate lowercase and uppercase characters
        lower = sorted([ch for ch in s if ch.islower()])
        upper = sorted([ch for ch in s if ch.isupper()])
        
        # Pointers for lowercase and uppercase lists
        i, j = 0, 0
        
        # Reconstruct the result string with sorted characters at correct case positions
        result = []
        for ch in s:
            if ch.islower():
                result.append(lower[i])
                i += 1
            else:
                result.append(upper[j])
                j += 1
        
        return ''.join(result)
