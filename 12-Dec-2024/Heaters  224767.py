# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
   
        houses.sort()
        heaters.sort()
        l=0
        r=0

        for house in houses:
            while l < len(heaters)- 1 and heaters[l] <= house:
                l += 1

            left = abs(house - heaters[l - 1])
            right = abs(heaters[l] - house)
            r = max(r, min(left, right))

        return r