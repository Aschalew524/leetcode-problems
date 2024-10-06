# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        cnt = Counter()
        for i,j in enumerate(s):
            cnt[j]=i
        left = 0
        right = 0
        for i,j in enumerate(s):
            right = max(right,cnt[j])
            if(i==right):
                ans.append(right-left+1)
                left = right + 1
        return ans



        
        