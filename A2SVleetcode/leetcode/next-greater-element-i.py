class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_check={num:i for i,num in enumerate(nums1)}
        ans=[-1]*len(nums1)
        stack=[]
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                temp=stack.pop()
                num_index = nums1_check[temp]
                ans[num_index]=nums2[i]
            if nums2[i] in nums1_check:
                stack.append(nums2[i])

        return ans
        