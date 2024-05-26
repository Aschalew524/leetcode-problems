# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return True

    def shortest(self, word: str) -> str:
        cur = self.root
        short = ""
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                return ""
            short += c
            cur = cur.children[idx]
            if cur.is_end:
                return short
        return short

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for s in dictionary:
            trie.insert(s)
        ans = ""
        for word in sentence.split(" "):
            shortest = trie.shortest(word)
            if len(shortest) != 0:
                ans += shortest + " "
            else:
                ans += word + " "
        return ans[:-1]