n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
lb,ub,ans=0,n,0
while lb<=ub:
    mid=(lb+ub)//2
    cow=1
    prev=l[0]
    for i in range(1,n):
        if l[i]-prev>=mid:
            cow+=1
            prev=l[i]
            if k==cow :
                break
    if cow==k:
        ans=mid
        lb=mid+1
    else:
        ub=mid-1
print(ans) 
