class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        ans = list(dominoes)

        slow = 0
        while slow<n and ans[slow]==".":
            slow+=1

        if slow<n and ans[slow]=="L":
            for i in range(slow):
                ans[i]="L"
        
        fast = slow+1
        while fast<n:
            while fast<n and ans[fast]==".":
                fast+=1
            
            if fast<n:
                if ans[slow]==ans[fast]:
                    for i in range(slow+1,fast):
                        ans[i] = ans[slow]
                elif ans[slow]=="R" and ans[fast]=="L":
                    for i in range((fast-slow-1)//2):
                        ans[slow+1+i]= "R"
                        ans[fast-1-i]="L"
            
                slow = fast
                fast +=1

        if slow<n and ans[slow]=="R":
            for i in range(slow+1,n):
                ans[i]="R"

        return "".join(ans)
    

print(Solution().pushDominoes(dominoes = ".L.R...LR..L.."))     # Output = "LL.RR.LLRRLL.."