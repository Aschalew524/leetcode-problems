class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans=""
        first=strs[0]
        last=strs[-1]
        for i in range(len(first)):
            if  first[i]!=last[i] or i==len(last):
                return ans
            ans+=first[i]
        return ans

        