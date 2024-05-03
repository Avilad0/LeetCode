class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        c1 = len(version1)
        c2 = len(version2)

        i=0
        while i<c1 and i<c2:
            t1 = int(version1[i])
            t2 = int(version2[i])

            if t1>t2:
                return 1
            elif t1<t2:
                return -1
            
            i+=1
        
        while i<c1:
            if int(version1[i])!=0:
                return 1
            i+=1
        
        while i<c2:
            if int(version2[i])!=0:
                return -1
            i+=1
            
        return 0
        