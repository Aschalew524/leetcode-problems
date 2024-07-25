# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A

t=int(input())
for i in range(t):
    n=int(input())
  
    if n% 7 == 0:
        print(n)
    else:
        x= n % 10
        n=n - x
        while n% 7 != 0:
            n+=1
        print(n)


    