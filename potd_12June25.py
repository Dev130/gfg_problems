import heapq

class Solution:
    def printKClosest(self, arr, k, x):
        candidates = []
        for val in arr:
            if val == x:
                continue
            distance = abs(val - x)
            candidates.append((distance, val))
        
        candidates.sort(key=lambda item: (item[0], -item[1]))
        
        result = []
        for i in range(min(k, len(candidates))):
            result.append(candidates[i][1])
            
        return result