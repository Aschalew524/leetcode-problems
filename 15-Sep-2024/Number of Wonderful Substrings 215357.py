# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        res, mask = 0, 0
        for c in word:
            idx = (ord(c) - ord('a'))
            mask ^= 1 << idx
            res += cnt[mask]
            for i in range(10):
                preMask = mask ^ (1 << i)
                res += cnt[preMask]
            cnt[mask] += 1
        return res