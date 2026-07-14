from typing import List
from collections import defaultdict

# sc=O(n), n =count(points)
# add: tc = O(1)
# count: tc = O(n) (worst case) (based on (O(count(X[point[x]])))
class DetectSquares:
    def __init__(self):
        self.X = defaultdict(lambda :defaultdict(int)) # x:dict(y1:freq,y2:freq...)
    
    def add(self, point: List[int]) -> None:
        x,y=point
        self.X[x][y]+=1
        

    def count(self, point: List[int]) -> int:
        ways = 0
        x1,y1 = point

        for y2 in self.X[x1].keys():
            side = y2-y1
            if side==0:
                continue

            x2 = x1+side
            ways += (self.X[x1][y2]*self.X[x2][y2]*self.X[x2][y1])
            
            x2 = x1-side
            ways += (self.X[x1][y2]*self.X[x2][y2]*self.X[x2][y1])

        return ways


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)