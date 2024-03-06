class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        minn=nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minn=min(nums[l],minn)
                break

            m=(l+r)//2
            minn=min(nums[m],minn)
            if nums[m] >= nums[r]:
                l=m+1
                
               

            else:
                r=m-1
        return minn


            
        