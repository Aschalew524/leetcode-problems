#with O(n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left , right = 0, 0
        res = 0
        d = {}
        maxFreq = 0
        while right < len(s):
            d[s[right]] = 1 + d.get(s[right],0)

            maxFreq = max(maxFreq,d[s[right]]) 

            while (right-left+1) - maxFreq > k:
                d[s[left]] -= 1
                left += 1
            res = max(res,(right-left+1))
            right += 1
        return res