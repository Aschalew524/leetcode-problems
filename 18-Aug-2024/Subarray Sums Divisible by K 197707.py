# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums, k) :
            dict = Counter()
            dict[0] =1
            cnt = 0
            Sum = 0
            for i in nums:
                Sum +=i
                m = Sum%k
                cnt += dict[m]
                dict[m]+=1
            return cnt