# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1
        queue = deque([(0, "0000")])
        
        while queue:
            step, code = queue.popleft()
            if(code==target):
                return step
            for i in range(4):
                d = int(code[i])
                for k in (d+1)%10,(d-1)%10:
                    cand = code[:i]+str(k)+code[i+1:]
                    if cand not in dead:
                        dead.add(cand)
                        queue.append((step+1, cand))
                        
        return -1