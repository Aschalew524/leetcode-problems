# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        root = [i for i in range(n)]
        rank = [0 for i in range(n)]
        heap = defaultdict(list)
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX]+=1
        for x, y in pairs:
            union(x, y)
    
        for i in range(n):
            heappush(heap[find(root[i])], s[i])
        ans = []
        for val in root:
            ans.append(heappop(heap[find(val)]))
        return ''.join(ans)