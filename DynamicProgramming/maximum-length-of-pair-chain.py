class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])
        cur = -float('inf')
        res = 0
        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                res += 1
        return res
