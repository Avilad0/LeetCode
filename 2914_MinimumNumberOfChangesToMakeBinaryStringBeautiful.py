class Solution:
    def minChanges(self, s: str) -> int:
        return sum( s[i]!=s[i+1] for i in range(0,len(s), 2))


        # minn = 0
        # for i in range(0, len(s),2):
        #     if s[i]!=s[i+1]:
        #         minn+=1
        # return minn