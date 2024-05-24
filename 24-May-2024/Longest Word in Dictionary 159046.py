# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=len)
        check=set()
        ans=""
        max_len=0
        for word in words:
            if len(word)==1:
                check.add(word)
            if word[:-1] in check :
                check.add(word)
                if len(word) > max_len:
                    max_len=len(word)
                    ans=word
                elif len(word) == max_len:
                    ans=min(ans,word)
        check=sorted(list(check))
        return ans if ans else check[0] if check else ans

        