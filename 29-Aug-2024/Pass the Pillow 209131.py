# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution(object):
    def passThePillow(self, n, time):
        count = 1
        flag = 1
        while time:
            time -= 1
            if flag:
                count += 1
                if count == n:
                    flag = not flag
            else:
                count -= 1
                if count == 1:
                    flag = not flag
        return count