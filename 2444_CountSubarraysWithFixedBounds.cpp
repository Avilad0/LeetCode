#include<bits/stdc++.h>
using namespace std;

// same complexity as below, but implemented in more efficient way.
// follows same principle of finding valid subarrays in a range based on last min, max, outOfrange numbers index.
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long count = 0;

        int n = nums.size(), lastMinIndex = -1, lastMaxIndex = -1, lastOutOfRangeIndex = -1;
        for (int i = 0; i<n; ++i){
            if (nums[i]<minK || nums[i]>maxK)   lastOutOfRangeIndex = i;

            if (nums[i]==minK)  lastMinIndex = i;
            if (nums[i]==maxK)  lastMaxIndex = i;

            if (min(lastMinIndex, lastMaxIndex) - lastOutOfRangeIndex>0)    count += min(lastMinIndex, lastMaxIndex) - lastOutOfRangeIndex;
        }

        return count;
    }
};


// // Same complexity as above, but more detailed and simple to understand.
// class Solution {
// private:
//     long long countInSub(vector<int>& nums, int minK, int maxK, int start, int end){
//         long long count = 0;
        
//         int minFreq = 0, maxFreq = 0, left=start;
//         for (int right=start; right<end; ++right){
//             if (nums[right]==minK) ++minFreq;
//             if (nums[right]==maxK) ++maxFreq;

//             while (minFreq>0 && maxFreq>0){
//                 count+= end - right;
//                 if (nums[left]==minK) --minFreq;
//                 if (nums[left]==maxK) --maxFreq;
//                 left++;
//             }
//         }

//         return count;
//     }

// public:
//     long long countSubarrays(vector<int>& nums, int minK, int maxK) {
//         long long count = 0;

//         int n = nums.size(), left = 0;
//         for (int right = 0; right<=n; ++right){
//             if (right==n || nums[right]<minK || nums[right]>maxK){
//                 if (left<right){
//                     count += countInSub(nums, minK, maxK, left, right);
//                 }
//                 left = right+1;
//             }
//         }

//         return count;
//     }
// };