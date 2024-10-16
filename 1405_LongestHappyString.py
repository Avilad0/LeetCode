import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, "a"))
        if b > 0:
            heapq.heappush(pq, (-b, "b"))
        if c > 0:
            heapq.heappush(pq, (-c, "c"))

        result = []
        while pq:
            count, character = heapq.heappop(pq)
            if len(result) >= 2 and result[-1] == character and result[-2] == character:
                if not pq:
                    break
                tempCnt, tempChar = heapq.heappop(pq)
                result.append(tempChar)
                if tempCnt  < -1:
                    heapq.heappush(pq, (tempCnt + 1, tempChar))
                heapq.heappush(pq, (count, character))
            else:
                result.append(character)
                if count < -1:
                    heapq.heappush(pq, (count+1, character))

        return "".join(result)