from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        lis=SortedList()
        ans=[]
        for n in nums[::-1]:
            count=bisect_left(lis,n)
            ans.append(count)
            lis.add(n)
        return reversed(ans)
