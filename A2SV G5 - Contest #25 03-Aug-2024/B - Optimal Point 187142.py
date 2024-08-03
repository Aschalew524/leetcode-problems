# Problem: B - Optimal Point - https://codeforces.com/gym/535749/problem/B

from typing import Counter


t=int(int(input()))
for i in range(t):
    n,k=map(int,input().split())
    cnt=Counter()
    for i in range(n):
        a,b=map(int,input().split())
        if a <= k <= b:
            for i in range(a,b+1):
                cnt[i]+=1
    lis=list(cnt.values())
    x=cnt[k]
    if len(cnt)== 0:
        print("NO")
    elif lis.count(x) > 1:
        print("NO")
    else:
        if len(cnt) > 0  and cnt[k] == max(cnt.values()):
            print("YES")
            
        else:
            print("NO")
   
        
    
    