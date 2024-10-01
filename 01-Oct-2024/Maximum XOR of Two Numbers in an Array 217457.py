# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Node:
    one=None
    zero=None
    def contains(self,bit):
        if bit:
            return self.one is not None
        return self.zero is not None
    def put(self,bit,node):
        if bit:
            self.one=node
        else:
            self.zero=node
    def get(self,bit):
        if bit:
            return self.one
        return self.zero
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,num):
        node=self.root
        for i in range(31,-1,-1):
            curr_bit=1 & (num>>i)
            if not node.contains(curr_bit):
                node.put(curr_bit,Node())
            node=node.get(curr_bit)
        
        
    def maxXOR(self,number):
        node=self.root
        ans=0
        for i in range(31,-1,-1):
            curr_bit=1 & (number>>i)
            if node.contains(1-curr_bit):
                node=node.get(1-curr_bit)
                ans|=(1<<i)
            else:
                node=node.get(curr_bit)
        return ans
        
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie=Trie()
        for num in nums:
            trie.insert(num)
        maxAns=0
        for num in nums:
            maxAns=max(maxAns,trie.maxXOR(num))
        return maxAns

        