# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next
            
       
        ans = [[-1 for _ in range(n)] for _ in range(m)]
       
        l, t, r, b = 0, 0, n - 1, m - 1
        idx = 0
        
        while l <= r and t <= b:
            for i in range(l, r + 1):
                if idx < len(values):
                    ans[t][i] = values[idx]
                    idx += 1
            t += 1
            
           
            for i in range(t, b + 1):
                if idx < len(values):
                    ans[i][r] = values[idx]
                    idx += 1
            r -= 1
            
            
            if t <= b:
                for i in range(r, l - 1, -1):
                    if idx < len(values):
                        ans[b][i] = values[idx]
                        idx += 1
                b -= 1
            

            if l <= r:
                for i in range(b, t - 1, -1):
                    if idx < len(values):
                        ans[i][l] = values[idx]
                        idx += 1
                l += 1
        
        return ans  