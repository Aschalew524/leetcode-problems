# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total= mean * (n + m)  
        rem_sum = total- sum(rolls)  
        if rem_sum < n or rem_sum > 6 * n:
            return []  
        base = rem_sum // n
        remainder = rem_sum % n
        result = [base] * n
        
        for i in range(remainder):
            result[i] += 1
        
        return result