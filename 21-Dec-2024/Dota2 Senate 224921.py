# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate):
        n, q1, q2 = len(senate), deque(), deque()

        for i,c in enumerate(senate):
            if c == "R":
                q1.append(i)
            else:
                q2.append(i)

        while q1 and q2:
            r, d = q1.popleft(), q2.popleft()

            if r < d:
                q1.append(r+n)
            else:
                q2.append(d+n)

        return "Radiant" if q1 else "Dire"


        