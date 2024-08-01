# Problem: A - Your Hackathon Project - Chat Feature - https://codeforces.com/gym/534160/problem/A

t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    i=n-1
    if n%2==0:
        while i >= n//2-1:
            if s[i] == ")":
                i-=1
            else:
                print("NO")
                break
        else:
            print("YES")
    else:
        while i > n//2-1:
            if s[i] == ")":
                i-=1
            else:
                print("NO")
                break
        else:
            print("YES")

        
        
        
            