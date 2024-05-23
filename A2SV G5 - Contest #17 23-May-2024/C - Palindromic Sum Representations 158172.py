# Problem: C - Palindromic Sum Representations - https://codeforces.com/gym/524965/problem/C

MOD = 10**9 + 7
def is_palindrome(num):
    return str(num) == str(num)[::-1]
max_len=40001
lis=[i for i in range(1,max_len) if is_palindrome(i)]
def check():
    dp = [0] * (max_len)
    dp[0] = 1
    for i in lis:
        for j in range(i,max_len):
            dp[j]= (dp[j]+dp[j-i] )% MOD
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = dp[n]
        print(result)
check()

    

 

   

   


    