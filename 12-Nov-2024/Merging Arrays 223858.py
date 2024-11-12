# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m = map(int,input().split())
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
l=0
r=0
ans=[]
while l<n and r<m:
    if list1[l] <= list2[r]:
        ans.append(list1[l])
        l+=1
    elif list1[l] > list2[r]:
        ans.append(list2[r])
        r+=1
if l<n:
    ans+=list1[l:]
if r<m:
    ans+=list2[r:]
print(*ans)
