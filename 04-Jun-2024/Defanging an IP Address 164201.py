# Problem: Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution(object):
    def defangIPaddr(self, address):
        lis=list(address)
        for i in range(len(lis)):
            if lis[i]==".":
                lis[i]="[.]"
        ans="".join(lis)
       
        return ans

        """
        :type address: str
        :rtype: str
        """
        