
class Solution:
  def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
    forbidden = set(forbidden)
    ans = 0
    r = len(word) - 1 

    for l in range(len(word) - 1, -1, -1):
      for j in range(l, min(l + 10, r + 1)):
        if word[l:j + 1] in forbidden:
          r = j - 1
          break
      ans = max(ans, r - l + 1)

    return ans