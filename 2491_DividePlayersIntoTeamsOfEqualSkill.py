from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n= len(skill)
        if n==2:
            return skill[0]*skill[1]
        
        summ = (sum(skill)*2.0)/n
        if summ != int(summ):
            return -1
        
        summ = int(summ)
        mapp = {}
        ans =0
        for x in skill:
            if abs(summ-x) in mapp:
                ans= ans + ((summ-x)*x)
                mapp[summ-x]-=1
                if mapp[summ-x]==0:
                    mapp.pop(summ-x)
            else:
                if x in mapp:
                    mapp[x]+=1
                else:
                    mapp[x]=1
        
        if mapp:
            return -1
        else:
            return ans