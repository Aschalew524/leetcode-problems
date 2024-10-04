# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        r = []
        middle = []
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i>pivot:
                r.append(i)
            elif i==pivot:
                middle.append(i)

        ans = l + middle +r
        return ans
