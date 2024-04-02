class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        st={}
        ts={}
        for i in range(len(s)):
            if ((s[i] in st) and st[s[i]]!=t[i]) or (t[i] in ts and ts[t[i]]!=s[i]):
                return False

            st[s[i]]=t[i]
            ts[t[i]]=s[i]       
        return True


        # m={}
        # l=[]
        # for i in range(len(s)):
        #     if s[i] not in m:
        #         if t[i] in l:
        #             return False
        #         m[s[i]] = t[i]
        #         l.append(t[i])
        #     elif m[s[i]]!=t[i]:
        #         return False
        
        # return True

print(Solution().isIsomorphic("add","egg"))
print(Solution().isIsomorphic("foo","bar"))
print(Solution().isIsomorphic("badc","baba"))