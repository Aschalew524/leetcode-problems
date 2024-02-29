class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel="aeiou"
        l=0
        count=0
        maxx=0

        for r in range(len(s)):
            if s[r] in vowel:
                count+=1
            if r-l+1>k:
                if s[l] in vowel:
                    count-=1
                l+=1
            maxx=max(count,maxx)
        return maxx