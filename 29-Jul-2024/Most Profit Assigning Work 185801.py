# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
            sorted_=sorted(worker)
            jobs=zip(difficulty,profit)
            sorted_jobs=sorted(jobs)
            n=len(sorted_jobs)
            best=0
            total_best=0
            i=0
            for skill in sorted_:
                while i<n and skill>=sorted_jobs[i][0]:
                    best=max(best, sorted_jobs[i][1])
                    i+=1
                total_best+=best
            return total_best        