from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        freq,ans,j = {},0,0
        
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1

            while freq[nums[i]]>k and j<=i:
                freq[nums[j]]-=1
                j+=1
            
            if i-j+1>ans:
                ans = i-j+1
            
        return ans
            

        # freq = {}
        # freq_arr=[]
        # ans = 0 
        # j=0
        # for i in range(len(nums)):
        #     if nums[i] in freq.keys():
        #         freq[nums[i]].append(i)
        #     else:
        #         freq[nums[i]]=[i]
        #     freq_arr.append(len(freq[nums[i]]))
        
        #     if freq_arr[i]<=k:
        #         continue
            
        #     if i-j>=ans:
        #         ans=i-j
            
        #     if freq[nums[i]][0] + 1>=j:
        #         j=freq[nums[i]][0] + 1

        #     freq[nums[i]] = freq[nums[i]][1:]
        #     for x in range(len(freq[nums[i]])):
        #         freq_arr[freq[nums[i]][x]]=x+1
            
        # if i-j+1>=ans:
        #     ans = i-j+1

        # return ans
    
print(Solution().maxSubarrayLength([1,2,3,1,2,3,1,2],2))
print(Solution().maxSubarrayLength([1],1))
print(Solution().maxSubarrayLength([1,2,2,1,3],1))
