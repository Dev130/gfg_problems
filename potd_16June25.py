class Solution:
    def minCost(self, heights, cost):
        n = len(heights)
        # Pair and sort by height
        paired = sorted(zip(heights, cost))
        
        # Step 1: Find weighted median
        total_cost = sum(cost)
        prefix = 0
        median_height = 0
        
        for h, c in paired:
            prefix += c
            if prefix >= (total_cost + 1) // 2:
                median_height = h
                break

        # Step 2: Calculate total cost to make all heights equal to median_height
        min_total_cost = 0
        for h, c in paired:
            min_total_cost += abs(h - median_height) * c

        return min_total_cost
