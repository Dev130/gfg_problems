class Solution:
    def kokoEat(self, arr, k):
        def canFinish(speed):
            hours = 0
            for bananas in arr:
                hours += (bananas + speed - 1) // speed  # equivalent to ceil
            return hours <= k
        
        low, high = 1, max(arr)
        answer = high
        
        while low <= high:
            mid = (low + high) // 2
            if canFinish(mid):
                answer = mid  # try a smaller speed
                high = mid - 1
            else:
                low = mid + 1
        
        return answer
