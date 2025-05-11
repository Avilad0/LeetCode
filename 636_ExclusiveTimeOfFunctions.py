from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stck = []
        time = [0]*n
        for log in logs:
            logList = log.split(":")     #id, state, timestamp
            logList[0], logList[2]  = int(logList[0]), int(logList[2])

            if logList[1] == "start":
                if len(stck)!=0:
                    time[stck[-1][0]] += logList[2] - stck[-1][2]
                stck.append(logList)
            else:
                time[logList[0]] += logList[2] - stck[-1][2] + 1
                stck.pop()
                if len(stck)!=0:
                    stck[-1][2] = logList[2]+1

        return time