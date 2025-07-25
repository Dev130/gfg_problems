class Solution:
    def findMajority(self, arr):
        n = len(arr)
        if not arr:
            return []

        # Step 1: Find at most two candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify actual counts
        res = []
        if candidate1 is not None and arr.count(candidate1) > n // 3:
            res.append(candidate1)
        if candidate2 is not None and candidate2 != candidate1 and arr.count(candidate2) > n // 3:
            res.append(candidate2)

        return sorted(res)
