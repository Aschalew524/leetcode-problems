class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
     
        possible=[]
        ans=[]
        for i,v in enumerate(arr):
            possible.append((abs(arr[i]-x),v))
        p=sorted(possible, key=lambda x:x[0])
        for i in range(k):
            ans.append(p[i][1])
        ans.sort()
        

        
        return ans
        