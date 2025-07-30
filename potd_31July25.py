class Solution:
    def powerfulInteger(self, intervals, k):
        from collections import defaultdict

        events = defaultdict(int)
        for l, r in intervals:
            events[l] += 1
            events[r+1] -= 1
        
        # All event points sorted
        sorted_points = sorted(events.keys())
        cnt = 0
        ans = -1

        for i, x in enumerate(sorted_points):
            cnt += events[x]
            # We care about the _previous_ segment, which ends here (at x-1)
            if cnt >= k:
                # Next event position or "infinity"
                if i + 1 < len(sorted_points):
                    nxt = sorted_points[i+1] - 1
                else:
                    nxt = x
                ans = max(ans, nxt)
        
        return ans
