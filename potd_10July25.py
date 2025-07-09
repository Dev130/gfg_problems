class Solution():
    def longestString(self, arr):
        sset = set(arr)
        res = ""
        for word in arr:
            isValid = True
            # Check all prefixes
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix not in sset:
                    isValid = False
                    break
            if isValid:
                # If this word is longer or lex smaller on tie
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
        return res
