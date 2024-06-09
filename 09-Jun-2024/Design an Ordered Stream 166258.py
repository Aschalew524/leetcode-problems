# Problem: Design an Ordered Stream - https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.values = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.values[idKey] = value
        res = []
        while self.ptr < len(self.values) and self.values[self.ptr] is not None:
            res.append(self.values[self.ptr])
            self.ptr += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)