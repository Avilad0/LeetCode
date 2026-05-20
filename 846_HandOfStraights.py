from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False

        freq = {}
        for h in hand:
            freq[h]=freq.get(h,0)+1
        
        for num in hand:
            start = num
            while start-1 in freq and freq[start-1]>0:
                start-=1
            while start<=num:
                while freq[start]:
                    for i in range(start,start+groupSize):
                        if i not in freq or freq[i]<=0:
                            return False
                        freq[i]-=1
                    
                start+=1

        
        return True