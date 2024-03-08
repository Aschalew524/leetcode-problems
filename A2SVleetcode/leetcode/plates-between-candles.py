class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        lis=[]
        count=0
        ans=[]
        res=[]
        for i in range(len(s)):
            if s[i]=="*":
                count+=1
                lis.append(count)
            elif s[i]=="|":
                lis.append(count)
                ans.append(i)

        for i in range(len(queries)):


            left=bisect_left(ans,queries[i][0] )
          
            
            right=bisect_right(ans,queries[i][1] )-1
            if left < right:
                res.append(lis[ans[right]]-lis[ans[left]])
            else:
                res.append(0)


        return res
        