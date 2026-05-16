from typing import List

import heapq
from collections import defaultdict, deque


# tc=O(len(tasks)), sc=O(26)=O(1), - maxHeap + deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
            
        freq = defaultdict(int)
        for task in tasks:
            freq[task]+=1
        
        q = deque() # (time, freq)

        maxHeap = []  # -freq
        for f in freq.values():
            heapq.heappush(maxHeap, -f)

        time = 0
        while q or maxHeap:
            time+=1
            # print(time, q, maxHeap)
            while q and q[0][0]+n<time:
                _, f = q.popleft()
                heapq.heappush(maxHeap, -f)
            
            if maxHeap:
                f = -heapq.heappop(maxHeap)
                if f>1:
                    q.append((time, f-1))
            else:
                time = q[0][0]+n
        
        return time
    

# tc=O(len(tasks)), sc=O(26)=O(1), - greedy - checking idle slots
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
            
        freq = [0]*26
        for task in tasks:
            freq[ord(task)-65]+=1
        
        freq.sort()
        maxFreq = freq[-1]
        idleSlots = (maxFreq-1)*n

        for i in range(24,-1,-1):
            # maxFreq-1 gaps can carry each item in freq[i]
            # if idleSlots get negative, the exisiting slots can be move 1 to left to accomodate other tasks without creating new idles. 
            # maximum idle slots will only be determined by maxFreq as calculated above, and overflows will not create more idle slots but readjustments will result in no idle slots.
            idleSlots -= min(maxFreq-1, freq[i])    

        return max(0,idleSlots) + len(tasks)        
        

# tc=O(len(tasks)), sc=O(26)=O(1), - math
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
            
        freq = [0]*26
        for task in tasks:
            freq[ord(task)-65]+=1
        
        # taking a ref from above, if idle slots exists, then, answer will be the time all the maxFreq items completes its last task, rest can be completed in between
        # if idle time not exists, then all tasks will be completed in len(tasks) time
        maxFreq, maxFreqCount = 0, 0
        for f in freq:
            if f>maxFreq:
                maxFreq, maxFreqCount = f, 1
            elif f==maxFreq:
                maxFreqCount+=1
        
        return max(len(tasks), (maxFreq-1)*(n+1) + maxFreqCount)