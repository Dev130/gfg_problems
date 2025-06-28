class Solution:
    def splitArray(self, arr, k):
        def can_split(max_sum):
            count = 1
            curr_sum = 0
            for num in arr:
                if curr_sum + num > max_sum:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return count <= k

        lo, hi = max(arr), sum(arr)
        answer = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                answer = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return answer
