class Solution:
    def isSumString(self, s):
        def isValidPart(x):
            return len(x) == 1 or x[0] != '0'  # No leading zero unless '0'
        
        def check(a, b, remaining):
            if not remaining:
                return True  # If nothing left, valid sum-string
            
            sum_str = str(int(a) + int(b))
            if remaining.startswith(sum_str):
                # Recurse with next pair (b, sum_str)
                return check(b, sum_str, remaining[len(sum_str):])
            else:
                return False
        
        n = len(s)
        
        # Try all possible first and second number splits
        for i in range(1, n):
            for j in range(i + 1, n):
                a = s[:i]
                b = s[i:j]
                
                if isValidPart(a) and isValidPart(b):
                    if check(a, b, s[j:]):
                        return True  # Found a valid sum-string
        
        return False  # No valid split found
