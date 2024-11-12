from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x: (x[0], -x[1]))
        queriesWithIndex = list(enumerate(queries))
        queriesWithIndex.sort(key = lambda x:x[1])
        n = len(items)

        itemIndex=0
        maxx = 0
        ans = [0]*len(queries)
        for (originalIndex, query) in queriesWithIndex:
            
            while itemIndex<n and items[itemIndex][0]<=query:
                if items[itemIndex][1]>maxx:
                    maxx = items[itemIndex][1]
                itemIndex+=1

            ans[originalIndex] = maxx
                
        return ans


# class Solution:
#     def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
#         items.sort(key = lambda x: (x[0], -x[1]))
#         n = len(items)
#         maxx = items[0][1]
#         for i in range(1,n):
#             if items[i][1]<maxx:
#                 items[i][1]=maxx
#             else:
#                 maxx = items[i][1]
        
#         def binarySearch (price) -> int:
#             if price < items[0][0]:
#                 return 0
#             if price>=items[n-1][0]:
#                 return items[n-1][1]

#             left, right  = 0 , n-1
#             while left<right:
#                 mid = (left+right)//2
#                 if items[mid][0]==price:
#                     return items[mid][1]
#                 if items[mid][0]<price:
#                     left = mid+1
#                 else:
#                     right = mid-1

#             if items[left][0]>price:
#                 left -=1

#             return items[left][1]

#         return [binarySearch(q) for q in queries]
    
print(Solution().maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]))