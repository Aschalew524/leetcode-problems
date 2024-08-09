# Problem: B - Fasika and Children - https://codeforces.com/gym/538762/problem/B

import math


n,m=map(int,input().split())
lis = list(map(int,input().split()))
check=[]
for i in range(n):
    check.append(math.ceil(lis[i]/m))
for i in range(n-1,-1,-1):
    if check[i] == max(check):
        print(i+1)
        break
else:
    print(n)