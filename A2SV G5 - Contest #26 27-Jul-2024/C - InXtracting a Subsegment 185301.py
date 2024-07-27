# Problem: C - InXtracting a Subsegment - https://codeforces.com/gym/537362/problem/C


n, k = map(int, input().split())
lis = list(map(int, input().split()))

if k == 1:
    print(min(lis))

elif k == 2:
    print(max(lis[0], lis[-1]))

else:
    print(max(lis))