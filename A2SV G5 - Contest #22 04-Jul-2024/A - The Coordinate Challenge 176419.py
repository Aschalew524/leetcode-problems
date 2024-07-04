# Problem: A - The Coordinate Challenge - https://codeforces.com/gym/531455/problem/A

for i in range(int(input())):
    n=int(input())
    rem=n % 3
    if n==1:
        print(2)

    elif n % 3 == 0:
        print(n//3)
    elif n % 3 == 2:
        print((n//3) + 1)
    elif n % 3 == 1:
        print((n-4)//3 + 2)

       
