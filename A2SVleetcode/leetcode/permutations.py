class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def swap(array, i, j):
            if i != j:
                array[i], array[j] = array[j], array[i]
        def b_track(arr,start):
            if start==len(nums):
                ans.append(arr[:])
            for i in range(start,len(nums)):
                swap(arr,i,start)
                b_track(arr,start+1)
                swap(arr,i,start)
        b_track(nums,0)
        return ans


                

                
        