import bisect
import math

class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        total_sum = sum(arr)

        unique_vals = sorted(list(set(arr)))
        val_to_coord = {val: i for i, val in enumerate(unique_vals)}
        max_coord = len(unique_vals)

        tree = [[0, 0] for _ in range(4 * max_coord)]

        def combine(res1, res2):
            if res1[0] > res2[0]:
                return res1
            elif res2[0] > res1[0]:
                return res2
            else:
                if res1[0] == 0:
                    return [0,0]
                return [res1[0], min(res1[1], res2[1])]

        def update_tree(node, start, end, idx, value, current_sum):
            if start == end:
                if value > tree[node][0]:
                    tree[node][0] = value
                    tree[node][1] = current_sum
                elif value == tree[node][0]:
                    tree[node][1] = min(tree[node][1], current_sum)
                return

            mid = (start + end) // 2
            if start <= idx <= mid:
                update_tree(2 * node + 1, start, mid, idx, value, current_sum)
            else:
                update_tree(2 * node + 2, mid + 1, end, idx, value, current_sum)
            
            tree[node] = combine(tree[2 * node + 1], tree[2 * node + 2])


        def query_tree(node, start, end, l, r):
            if r < start or end < l:
                return [0, 0]
            if l <= start and end <= r:
                return tree[node]

            mid = (start + end) // 2
            p1 = query_tree(2 * node + 1, start, mid, l, r)
            p2 = query_tree(2 * node + 2, mid + 1, end, l, r)
            return combine(p1, p2)

        for x in arr:
            compressed_x = val_to_coord[x]

            if compressed_x > 0:
                prev_lis_info = query_tree(0, 0, max_coord - 1, 0, compressed_x - 1)
            else:
                prev_lis_info = [0, 0]

            current_lis_length = prev_lis_info[0] + 1
            current_lis_sum = prev_lis_info[1] + x

            update_tree(0, 0, max_coord - 1, compressed_x, current_lis_length, current_lis_sum)

        overall_max_lis_info = query_tree(0, 0, max_coord - 1, 0, max_coord - 1)
        min_lis_sum = overall_max_lis_info[1]

        return total_sum - min_lis_sum