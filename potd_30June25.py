class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)

        # Helper function to check if a target height is possible
        def is_possible(target):
            add = [0] * (n + 1)
            curr_add = 0
            k_remaining = k

            for i in range(n):
                curr_add += add[i]
                height = arr[i] + curr_add
                if height < target:
                    delta = target - height
                    if delta > k_remaining:
                        return False
                    k_remaining -= delta
                    curr_add += delta
                    if i + w < n:
                        add[i + w] -= delta
            return True

        # Binary search
        low = min(arr)
        high = min(arr) + k + w + 1  # upper bound large enough

        result = low
        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
