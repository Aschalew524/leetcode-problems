class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def b_track(i,comb,summ):
            if summ==target:
                ans.append(comb.copy())
                return
            if i >= len(candidates) or summ > target:
                return
            candidates[i]
            comb.append(candidates[i])
            b_track(i,comb,summ+candidates[i])
            comb.pop()
            b_track(i+1,comb,summ)
        b_track(0,[],0)
        return ans


    
        