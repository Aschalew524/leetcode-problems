class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        b = [0] * len(a)
        for i in a:
            b[int(i[-1]) - 1] = i[0:-1]
        return " ".join(b)