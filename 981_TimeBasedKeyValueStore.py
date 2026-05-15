class TimeMap:

    def __init__(self):
        self.map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:

        curr = self.map.get(key, [])
        ans = ""
        left, right = 0, len(curr)-1
        while left<=right:
            mid = (left+right)//2
            if timestamp<curr[mid][0]:
                right=mid-1
            else:
                ans = curr[mid][1]
                left=mid+1

        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)