import heapq
from collections import Counter

class Solution:
    def minValue(self, s, k):
        # Count frequencies
        freq = Counter(s)
        
        # Use a max-heap, so we push negatives (heapq is min-heap by default)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        # Remove k characters
        while k > 0 and max_heap:
            top = -heapq.heappop(max_heap)
            top -= 1
            k -= 1
            if top > 0:
                heapq.heappush(max_heap, -top)
        
        # Calculate the sum of squares of frequencies
        return sum(x * x for x in map(lambda x: -x, max_heap))
