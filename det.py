def det(n,a):
    if n==1:
        return a[0][0]
    k=-1
    s=0
    for i in range(n):
        k*=(-1)
        b=[]
        for p in range(1,n):
            b.append(list(a[p]))
        for t in range(n-1):
            b[t].pop(i)
        s+=k*a[0][i]*det(n-1,b)
        
    return s
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
print(det(n,a))
