class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        s = sorted(nums)
        idx= {}
        for i in range(len(nums)):
            if s[i] not in idx:
                idx[s[i]] = i
        for i in range(len(nums)):
            res.append(idx[nums[i]])
        return res