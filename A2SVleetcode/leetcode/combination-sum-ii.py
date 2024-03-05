class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def b_track(start,curr,target):
            if target==0:
                ans.append(curr.copy())
                return 
            if target < 0:
                return 
            prev=float("-inf")
            for i in range (start,len(candidates)):
                if candidates[i]==prev:
                    continue
                curr.append(candidates[i])
                b_track(i+1,curr,target-candidates[i])
                curr.pop()
                prev=candidates[i]
        b_track(0,[],target)
        return ans
            
        