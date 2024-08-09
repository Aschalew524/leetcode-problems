# Problem: A - Split the Set - https://codeforces.com/gym/538762/problem/A

t = int(input())
for i in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    odd = 0
    even = 0
    for i in range(len(lis)):
        if lis[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == even == n:
        print("YES")
    else:
        print("NO")