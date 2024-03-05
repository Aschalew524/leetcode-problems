class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        def b_track(start,subs):
            ans.append(subs[:])
                 
            
            for i in range(start, n):
                subs.append(nums[i])
                b_track(i+1,subs)
                subs.pop()
        b_track(0,[])
        res=[]
        
        for i in ans:
            if not i in res:
                res.append(i)
        return res

        
        