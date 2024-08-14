# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i] >= 0 :
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        l=0
        r=0
       
        while l < len(pos) and r < len(neg):
            ans.append(pos[l])
            ans.append(neg[r])
            l+=1
            r+=1
        while  l < len(pos):
            ans.append(pos[l])
            l+=1
        while r < len(neg):
            ans.append(neg[r])
            r+=1
        return ans

            



        