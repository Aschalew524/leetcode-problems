# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        lis = [0]*(n+1)

        for fir, sec, seats in bookings:
            lis[fir-1]+= seats
            lis[sec]-= seats

        return list(accumulate(lis[:-1]))