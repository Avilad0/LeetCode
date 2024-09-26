from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.calendar.bisect_right((start, end))
        if (idx > 0 and self.calendar[idx-1][1] > start) or (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
        self.calendar.add((start, end))
        return True
    
'''
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        
        if len(self.events)==0 or start >= self.events[-1][1]:
            self.events.append([start, end])
            return True
        if end<= self.events[0][0]:
            self.events.insert(0, [start, end])
            return True
        
        if start<=self.events[0][0] or end>=self.events[-1][1]:
            return False

        left = 0
        right = len(self.events) -1
        mid = 0

        while left<right:
            mid = (left + right)//2
            if self.events[mid][0] == start or self.events[mid][1]==end:
                return False
            
            if self.events[mid][0]<start:
                left = mid + 1
            else:
                right = mid -1

        if self.events[mid][0]>=end and self.events[mid-1][1]<=start:
            self.events.insert(mid, [start, end])
            return True
        
        if self.events[mid][1]<=start and self.events[mid+1][0]>=end:
            self.events.insert(mid, [start, end])
            return True
        
        return False

'''


obj = MyCalendar()
print(obj.book(47,50))
print(obj.book(33,41))
print(obj.book(39,45))
print(obj.book(33,42))
print(obj.book(25,32))
print(obj.book(26,35))

# [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]

