# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans=[False]*len(candies)
        max_=max(candies)
        for i,v in enumerate(candies):
            if v+extraCandies >= max_:
                ans[i]=True
        return ans
           


        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        