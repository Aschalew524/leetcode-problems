class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n%2==0:
            return (pow(5,n//2,1000000007)*pow(4,n//2,1000000007)%((10**9)+7))
        else:
            return (pow(5,n//2+1,1000000007)*pow(4,n//2,1000000007)%((10**9)+7))  