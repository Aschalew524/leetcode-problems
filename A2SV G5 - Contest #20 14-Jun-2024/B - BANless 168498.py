# Problem: B - BANless - https://codeforces.com/gym/528792/problem/B

for i in range(int(input())):
    n=int(input())
    s="BAN"*n
    ans=[]
    l=0
    r=len(s)-1
    count=0
    while l < r:
        ans.append((l+1,r+1))
        count+=1
        r-=3
        l+=3
    print(count)
    for an in ans:
        print(*an)




