# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n=len(weights)
    
        def possible(capacity):
            cnt=1
            weight=0
            for i in range(n):
                weight+=weights[i]
                if weight > capacity:
                    cnt+=1
                    weight=weights[i]
                if cnt > days:
                    return False
            return True 
        def bs(weights):
            l=max(weights)
            r=sum(weights)
            best=r
            while l <= r:
                m=(l+r)//2
                if not possible(m):
                    l=m+1
                else:
                    best=m
                    r=m-1
            return best
        return bs(weights)
            





