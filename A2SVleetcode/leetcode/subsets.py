class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def b_track(start,subs):
            ans.append(subs[:])
                 
            
            for i in range(start, n):
                subs.append(nums[i])
                b_track(i+1,subs)
                subs.pop()
        b_track(0,[])
        return ans

        