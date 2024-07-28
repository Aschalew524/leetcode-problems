# Problem: B - Mohammed's Magical Cleaning Machine - https://codeforces.com/gym/537362/problem/B

t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    count=0
    i=0
    while i < n and lis[i]==0:
        i+=1
    for j in range(i,n-1):
        count+=lis[j]
        if lis[j]==0:
            count+=1
    print(count)
    