from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0]*n
        indexedNums = [(nums[i],i) for i in range(n)]

        def mergeSort(start, end):
            if start>=end:
                return 0

            mid = start + ((end-start+2)//2)
            mergeSort(start, mid-1)
            mergeSort(mid, end)
            
            temp = []
            i,j = start,mid
            currentCount = 0
            while i<=mid-1 and j<=end:
                if indexedNums[i][0]<=indexedNums[j][0]:
                    temp.append(indexedNums[i])
                    counts[indexedNums[i][1]]+=currentCount
                    i+=1
                else:
                    temp.append(indexedNums[j])
                    currentCount+=1
                    j+=1
                
            while i<=mid-1:
                temp.append(indexedNums[i])
                counts[indexedNums[i][1]]+=currentCount
                i+=1
            while j<=end:
                temp.append(indexedNums[j])
                j+=1

            for i in range(start,end+1):
                indexedNums[i]=temp[i-start]


        mergeSort(0,n-1)
        return counts
    

print(Solution().countSmaller(nums = [5,2,6,1]))    #[2,1,1,0]