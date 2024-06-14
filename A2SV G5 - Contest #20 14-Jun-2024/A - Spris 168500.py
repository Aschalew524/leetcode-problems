# Problem: A - Spris - https://codeforces.com/gym/528792/problem/A

a = int(input())
b = int(input())
c = int(input())

ma = a
av = b // 2
ban = c // 4

tot= min(ma, av, ban)
print(tot* 7)