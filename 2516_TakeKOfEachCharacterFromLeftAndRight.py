class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0]*3
        for c in s:
            count[ord(c)-97]+=1
        
        for c in count:
            if c<k:
                return -1
            
        windowCount = [0]*3
        left,right=0,0
        maxRemovalWindow = 0

        for right in range(len(s)):
            windowCount[ord(s[right])-97]+=1

            while left<=right and ( (count[0]-windowCount[0]<k) or (count[1]-windowCount[1]<k) or (count[2]-windowCount[2]<k) ):
                windowCount[ord(s[left])-97]-=1
                left+=1
            
            maxRemovalWindow = max(maxRemovalWindow, right-left+1)
            
        return len(s)-maxRemovalWindow