class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		res = 0 
		p_sum = 0
		d = {0 : 1}

		for num in nums:
		
			p_sum = p_sum + num

			if p_sum - k in d:
			
				res = res + d[p_sum - k]

			if p_sum not in d:
			
				d[p_sum] = 1
			else:
				d[p_sum] = d[p_sum] + 1

		return res