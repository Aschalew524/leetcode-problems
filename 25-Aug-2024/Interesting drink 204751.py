# Problem: Interesting drink - https://codeforces.com/problemset/problem/706/B/

n = int(input())
prices = list(map(int, input().split()))
prices.sort()
q = int(input())
 
for i in range(q):
    m = int(input())
    l = 0
    r = len(prices) - 1
    while l <= r:
        mid = (l + r) // 2
        if prices[mid] <= m:
            l = mid + 1
        else:
            r = mid - 1
    count = l
    print(count)