class Solution:
    unique = set()
    maxx = 1
    n = None
    def parse(self, s, i):
        if i==self.n:
            if len(self.unique)> self.maxx:
                self.maxx = len(self.unique)
            return

        temp = ""
        for j in range(i,self.n):
            temp+=s[j]
            if temp not in self.unique:
                self.unique.add(temp)
                self.parse(s,j+1)
                self.unique.remove(temp)


    def maxUniqueSplit(self, s: str) -> int:
        self.n = len(s)
        self.parse(s,0)
        return self.maxx
    


'''
s = "wwwzfvedwfvhsww" ans=11

wwwzfvedwfvhsww
w ww z f v e d wf vh sww   //10
www z f v e d w fv h s ww  //11
www z f v e dw fv h sw w  //11

unique chars = 8 
w = 3,1,2 = 6 
f = 1,1 = 2
v = 1,1 = 2

8 + 2(w,ww) + 1 (fv)

'''