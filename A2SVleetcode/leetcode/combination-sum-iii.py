class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        nums=[1,2,3,4,5,6,7,8,9]
        def comb(start,curr,n):
            if n==0 and len(curr)==k:
                ans.append(curr.copy())
                return
            if n < 0 :
                return
            for i in range(start,len(nums)):
                curr.append(nums[i])
                comb(i+1,curr,n-nums[i])
                curr.pop()
        comb(0,[],n)
        return ans


            
            

        