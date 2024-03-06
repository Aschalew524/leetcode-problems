# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=0
        r=n
        while l<=r:
            i=(l+r)//2
            if guess(i)==0:
                return i
            elif guess(i)==-1:
                r=i-1
            else:
                l=i+1
        