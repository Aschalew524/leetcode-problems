# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True
    def search(self, word: str) -> bool:
        def dfs( word,cur):
            for i in range(len(word)):
                char = word[i]
                if char == ".":
                    for j in range(26):
                        if cur.children[j] and dfs(word[i+1:], cur.children[j]):
                            return True
                    return False
                

                idx = ord(char) - ord('a')
                if not cur.children[idx]:
                    return False
                
                cur = cur.children[idx]

            return cur.is_end

        return dfs(word, self.root)


            
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)