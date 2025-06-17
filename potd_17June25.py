import bisect

class Solution:
    def minimumCoins(self, arr, k):
        n = len(arr)
        if n <= 1:
            return 0

        arr.sort()

        # Calculate prefix sums
        prefix_sum = [0] * n
        prefix_sum[0] = arr[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + arr[i]

        min_removed_coins = float('inf')

        # Iterate through each element as the potential minimum value in the remaining piles
        for i in range(n):
            current_min_val = arr[i]

            # Coins to remove from piles smaller than current_min_val
            # These are piles arr[0]...arr[i-1]
            coins_removed_from_smaller = 0
            if i > 0:
                coins_removed_from_smaller = prefix_sum[i-1]

            # Find the upper bound for piles that must be trimmed or entirely removed
            # These are piles where value > current_min_val + k
            target_max_val = current_min_val + k
            
            # bisect_right returns an insertion point which comes after (to the right of) 
            # any existing entries of value x in a.
            # So, arr[upper_bound_idx] will be the first element > target_max_val
            upper_bound_idx = bisect.bisect_right(arr, target_max_val)

            coins_removed_from_larger_by_trimming = 0
            if upper_bound_idx < n:
                # These are piles from arr[upper_bound_idx] to arr[n-1]
                # Sum of coins in these piles before trimming
                total_sum_above_range = prefix_sum[n-1] - (prefix_sum[upper_bound_idx-1] if upper_bound_idx > 0 else 0)
                
                # Number of piles to be trimmed
                num_piles_to_trim = n - upper_bound_idx
                
                # Desired sum of these piles if they are all trimmed to target_max_val
                desired_sum_after_trimming = num_piles_to_trim * target_max_val
                
                coins_removed_from_larger_by_trimming = total_sum_above_range - desired_sum_after_trimming

            current_total_removed = coins_removed_from_smaller + coins_removed_from_larger_by_trimming
            min_removed_coins = min(min_removed_coins, current_total_removed)

        return min_removed_coins