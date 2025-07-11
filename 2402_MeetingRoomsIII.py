from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        roomCounts = [0]*n
        roomsAvailableHeap = [] #roomnumber
        for i in range(n):
            heapq.heappush(roomsAvailableHeap, i) 
        
        roomsBookedHeap = []    # endtime, roomnumber
    
        meetings.sort()
        meetingLen = len(meetings)

        for meetingIndex in range(meetingLen):
            startI, endI = meetings[meetingIndex][0], meetings[meetingIndex][1]

            while roomsBookedHeap and roomsBookedHeap[0][0]<=startI:
                (_, selectedRoom) = heapq.heappop(roomsBookedHeap)
                heapq.heappush(roomsAvailableHeap, selectedRoom)
        
            if roomsAvailableHeap:
                selectedRoom = heapq.heappop(roomsAvailableHeap)
                heapq.heappush(roomsBookedHeap, (endI, selectedRoom))
                roomCounts[selectedRoom]+=1
            else:
                (nextAvailableTime, selectedRoom) = heapq.heappop(roomsBookedHeap)
                heapq.heappush(roomsBookedHeap, (nextAvailableTime + endI-startI, selectedRoom))
                roomCounts[selectedRoom]+=1


        return roomCounts.index(max(roomCounts))
    

print(Solution().mostBooked(n = 4, meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]])) #output = 0
print(Solution().mostBooked(n = 2, meetings = [[4,11],[1,13],[8,15],[9,18],[0,17]])) #output = 1


'''
n = 4, meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]]
Expected = 0


[ [2,13], [3,12], [7,10], [17,19], [18,19]]

rooms : 
0   [2,13]  [17,19]
1   [3,12]  [18,19]
2   [7,10]
3   


n = 2 meetings = [[4,11],[1,13],[8,15],[9,18],[0,17]]
Expected = 1

[ [0,17], [1,13], [4,11], [8,15], [9,18] ]

rooms:
0   [0,17]  [8,15]=[17,24]
1   [1,13]  [4,11]=[13,20]  [9,18]=[20,29]

'''