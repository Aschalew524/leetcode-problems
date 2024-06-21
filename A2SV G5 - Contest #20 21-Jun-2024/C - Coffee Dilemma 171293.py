# Problem: C - Coffee Dilemma - https://codeforces.com/gym/528792/problem/C

import heapq
n = int(input())
lis = list(map(int, input().split()))
heap = []
total = 0
for i in lis:
	total += i
	heapq.heappush(heap, i)
	while total < 0:
		total -= heapq.heappop(heap)

print(len(heap))