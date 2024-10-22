# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap=[-i for i in nums]
        heapify(heap)
        ans=0
        while k > 0:
            n=heappop(heap)
            ans+=n
            m=math.ceil(-(n/3))
            heappush(heap,-m)
            k-=1
        return -ans



    

     
        