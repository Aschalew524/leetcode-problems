# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius):
        res=[]
        res.append(celsius + 273.15)
        res.append(celsius * 1.80 + 32.00)
        return res