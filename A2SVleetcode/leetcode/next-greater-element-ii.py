class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        m_stack = []
        n=len(nums)
        res = [-1] * n

        for i in range(n*2):
            idx = i % n
            while m_stack and nums[m_stack[-1]] < nums[idx]:
                res[m_stack.pop()] = nums[idx]
            m_stack.append(idx)
        return res