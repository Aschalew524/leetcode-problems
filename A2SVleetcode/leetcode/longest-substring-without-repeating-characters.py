class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        l=0
        longest=0
        seen={}
        for r in range(len(s)):
            if s[r] in seen:
                seen[s[r]]+=1
                while seen[s[r]]>1:
                    seen[s[l]]-=1
                    l+=1
            else:
                seen[s[r]]=1
            longest=max(longest,r-l+1)
        
        return longest