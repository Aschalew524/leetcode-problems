class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        
        def b_track(start,comb):
            if len(comb)==k:
                ans.append(comb[:])
                return 
            
            for i in range(start, n+1):
                comb.append(i)
                b_track(i+1,comb)
                comb.pop()
        b_track(1,[])
        return ans



        