class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 
        l, r = 0, len(people) - 1 
        count=0
        while l<= r:
            diff=limit - people[r]
            r-=1
            count+=1
            
            if l <= r and people[l] <= diff:
                l+=1
        return count