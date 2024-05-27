# Problem: D - BitPleasure Maximization - https://codeforces.com/gym/526229/problem/D

class TrieNode:
    def __init__(self):
        self.ind = None
        self.children = [None for _ in range(2)]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, i):
        cur = self.root
        for ch in range(len(word)):
            order = int(word[ch])
            if not cur.children[order]:
                cur.children[order] = TrieNode()
            cur = cur.children[order]
        cur.ind = i

    def search(self, word):
        cur = self.root
        for ch in range(len(word)):
            order = abs(int(word[ch])-1)
            order1 = int(word[ch])
            if not cur.children[order]:
                if cur.ind:
                    return cur.ind
                else:
                    cur = cur.children[order1]
                    continue
            cur = cur.children[order]
        return cur.ind


n = int(input())

lis = [int(_) for _ in input().split()]

pre = [lis[0]]
post = [lis[-1]]

for i in range(1, n):
    pre.append(pre[-1] ^ lis[i])
for j in range(n-2, -1, -1):
    post.append(post[-1] ^ lis[j])
trie = Trie()
maxiPo = len(bin(max(post))[2:])
maxiPr = len(bin(max(pre))[2:])
maxi = max(maxiPo, maxiPr)
for i, val in enumerate(post):
    b = bin(val)[2:]
    l = len(b)
    trie.insert((maxi-l)*"0"+b, i)
ans = max(pre[0], post[0], pre[-1], post[-1])
for i in range(len(pre)-1):
    b = bin(pre[i])[2:]
    l = len(b)
    index = trie.search((maxi-l)*"0"+b)
    ans = max(ans, pre[i] ^ post[index])
print(max(ans, max(pre), max(post)))