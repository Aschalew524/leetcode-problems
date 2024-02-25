class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans=[]
        unique=set()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
        
                if nums[i]+nums[left]+nums[right]==0:
                    sublist=(nums[i],nums[left],nums[right])
                    unique.add(sublist)
                    left+=1
                    right-=1
                elif nums[i]+nums[left]+nums[right]<0:
                    left+=1
                else:
                    right-=1
        ans = [list(triplet) for triplet in unique]
        return ans


        