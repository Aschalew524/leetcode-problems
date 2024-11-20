# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        pre = [0]*n
        suf = [0]*n
        left_count = 0
        for i in range(1,n):
            pre[i] = pre[i-1]+int(boxes[i-1])+left_count
            if boxes[i-1]=="1":
                left_count += 1
        
        right_count = 0
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1]+int(boxes[i+1])+right_count
            if boxes[i+1]=="1":
                right_count+=1
        return [i+j for i,j in zip(pre, suf)]