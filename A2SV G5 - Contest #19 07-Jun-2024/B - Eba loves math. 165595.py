# Problem: B - Eba loves math. - https://codeforces.com/gym/527294/problem/B

t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    ans=lis[0]
    for i in range(1,n):
        ans=lis[i] & ans
    print(ans)

    