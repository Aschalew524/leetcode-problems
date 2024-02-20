class Solution:
    def longestPalindrome(self, s: str) -> int:
        k,p=1,0
        if len(set(s))==1:
            return len(s)
        c=Counter(s)
        for i in c:
            if c[i]%2==0:
                p+=c[i]
            if c[i]%2!=0:
                if k==1:
                    p+=c[i]
                    k=0
                else:
                    p+=(c[i]-1)
        return p