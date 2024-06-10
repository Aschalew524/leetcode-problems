# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        duration = [1, 7, 30]
        min_cost = float('inf')
        def dp(idx):
            nonlocal min_cost
            if idx >= len(days):
                return 0
            if idx in memo:
                return memo[idx]
            j = idx
            for i in range(3):
                while j < len(days) and days[j] < days[idx] + duration[i]:
                    j += 1

                min_cost = min(min_cost, dp(j) + costs[i])

            memo[idx] = min_cost
            return memo[idx]

        return dp(0)