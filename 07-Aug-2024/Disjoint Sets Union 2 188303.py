# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

n, q = map(int, input().split())
parent = list(range(n + 1))
size = [1] * (n + 1)
min_val = [i for i in range(n + 1)]
max_val = [i for i in range(n + 1)]
def find_parent(i):
    if i != parent[i]:
        parent[i] = find_parent(parent[i])
    return parent[i]

def unite(x, y):
    rootX = find_parent(x)
    rootY = find_parent(y)

    if rootX == rootY:
        return

    if size[rootX] > size[rootY]:
        rootX, rootY = rootY, rootX

    parent[rootX] = rootY
    size[rootY] += size[rootX]
    min_val[rootY] = min(min_val[rootY], min_val[rootX])
    max_val[rootY] = max(max_val[rootY], max_val[rootX])


   

for _ in range(q):
    inp = input().split()
    if inp[0] == "union":
        u, v = map(int, inp[1:])
        unite(u, v)
    else:
        u = find_parent(int(inp[1]))
        print(min_val[u], max_val[u], size[u])


