class Solution:
    def numberOfInversions(self, nums):
        n = len(nums)

        def mergeSort(start, end):
            if start>=end:
                return 0

            mid = start + ((end-start+2)//2)
            count = mergeSort(start, mid-1) + mergeSort(mid, end)
            
            temp = []
            i,j = start,mid
            while i<=mid-1 and j<=end:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    count+=mid-i
                    j+=1
                
            while i<=mid-1:
                temp.append(nums[i])
                i+=1
            while j<=end:
                temp.append(nums[j])
                j+=1

            for i in range(start,end+1):
                nums[i]=temp[i-start]

            return count

        return mergeSort(0,n-1)


print(Solution().numberOfInversions([-10, -5, 6, 11, 15, 17]))