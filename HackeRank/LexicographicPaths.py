#x=col, y=row. 
#consider (x,y) as points on cartesan plane. So m,n = y+1, x+1
# k is 0 index, so considering k+1 
def solve(x, y, k):

    m,n,newk = y+1,x+1,k+1
    factorials = [1]
    for i in range(1, m + n - 1):
        factorials.append(factorials[i-1] * i)

    total = factorials[m+n-2]//(factorials[m-1]*factorials[n-1])

    if k>total:
        return ""
    
    ans = []
    while newk>0 and m>1 and n>1:
        startsWithH = factorials[m+n-3]/(factorials[m-1]*factorials[n-2])
        if newk<=startsWithH:
            ans.append('H')
            n-=1
        else:
            ans.append('V')
            m-=1
            newk-=startsWithH
        
    while n>1:
        ans.append('H')
        n-=1

    while m>1:
        ans.append('V')
        m-=1

    return "".join(ans)


# print(solve(4,4,2))

# print(solve(2,2,3))
# print(solve(2,2,2))

print(solve(7,5,582))  #VHHVVVHHHHHV