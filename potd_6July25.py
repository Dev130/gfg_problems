import heapq

class Solution:
    def topKSumPairs(self, a, b, k):
        n = len(a)
        # Sort both arrays descending
        a.sort(reverse=True)
        b.sort(reverse=True)
        
        # Max-heap: use negatives to simulate max-heap with heapq
        heap = []
        # Set to track visited (i,j) pairs
        visited = set()
        
        # Start with the largest sum
        heapq.heappush(heap, (-(a[0] + b[0]), 0, 0))
        visited.add((0,0))
        
        result = []
        
        for _ in range(k):
            sum_neg, i, j = heapq.heappop(heap)
            result.append(-sum_neg)
            
            # Next pair in a
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(heap, (-(a[i+1] + b[j]), i+1, j))
                visited.add((i+1, j))
            
            # Next pair in b
            if j + 1 < n and (i, j+1) not in visited:
                heapq.heappush(heap, (-(a[i] + b[j+1]), i, j+1))
                visited.add((i, j+1))
        
        return result
