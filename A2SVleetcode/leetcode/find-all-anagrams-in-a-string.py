class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sdict = {}
        pdict = {}
        if len(p) > len(s):
            return []
        for i in range(len(p)):
            pdict[p[i]] = pdict.get(p[i], 0) + 1
            sdict[s[i]] = sdict.get(s[i], 0) + 1
        res = []
        if pdict == sdict:
            res = [0]
        l = 0
        for r in range(len(p), len(s)):
            sdict[s[r]] = sdict.get(s[r], 0) + 1
            sdict[s[l]] -= 1
            if sdict[s[l]] == 0:
                sdict.pop(s[l])
            l += 1
            if pdict == sdict:
                res.append(l)
        return res