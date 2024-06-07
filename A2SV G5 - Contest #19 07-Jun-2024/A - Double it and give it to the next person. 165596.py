# Problem: A - Double it and give it to the next person. - https://codeforces.com/gym/527294/problem/A

t=int(input())
for i in range(t):
    st=""
    ans=""
    res=""
    s=input()
    for c in s:
        st+=c
        st+=c
    st=sorted(st)
    for r in range(0,len(st),2):
        ans+=st[r]
        if r+1 < len(st):
            res+=st[r+1]
    res=sorted(res,reverse=True)
    res="".join(res)
    print(ans+res)
    
    


