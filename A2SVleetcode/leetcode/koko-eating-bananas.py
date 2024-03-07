class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r, best = 1, max(piles), -1
        while l <= r:
            mid = l+(r-l)  // 2
            hour = 0
            for i in range(len(piles)):
                hour += ceil(piles[i] / mid)
            if hour > h:
                l = mid + 1

            else:
                r = mid - 1
                best = mid
        return best