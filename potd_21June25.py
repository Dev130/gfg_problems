class Solution:
    def catchThieves(self, arr, k):
        police = []
        thief = []
        count = 0

        for i in range(len(arr)):
            if arr[i] == 'P':
                police.append(i)
            elif arr[i] == 'T':
                thief.append(i)

        # Match police and thieves
        while police and thief:
            if abs(police[0] - thief[0]) <= k:
                count += 1
                police.pop(0)
                thief.pop(0)
            elif police[0] < thief[0]:
                police.pop(0)
            else:
                thief.pop(0)

        return count
