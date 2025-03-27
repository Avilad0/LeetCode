#include<bits/stdc++.h>
using namespace std;

// Boyer-Moore Majority Voting Algorithm
// tc = O(n), sc = O(1)
class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        int n=nums.size(), dominantVal=nums[0], dominantFreq=1, i;
        for (i=1; i<n; ++i){
            if (dominantVal==nums[i]){
                ++dominantFreq;
            } else {
                --dominantFreq;
            }

            if (dominantFreq==0){
                dominantVal = nums[i];
                dominantFreq = 1;
            }
        }

        dominantFreq = 0;
        for (i=0;i<n;++i)   
            if (dominantVal == nums[i])
                ++dominantFreq;

        if (n%2==1 && dominantFreq <= (n+1)/2){
            return -1;
        }

        int currDominantCount = 0;
        for (i=0 ;i<n; ++i){
            if (nums[i]==dominantVal){
                ++currDominantCount;
                if (currDominantCount > (i+1)/2){
                    break;
                }
            }
        }

        return i;
    }
};

// // tc = O(n), sc = O(n)
// class Solution {
// public:
//     int minimumIndex(vector<int>& nums) {
//         unordered_map<int, int> freq;
//         int n=nums.size(), dominantVal, dominantFreq=0;
//         for (auto& num: nums){
//             ++freq[num];
//             if (freq[num]>dominantFreq){
//                 dominantFreq = freq[num];
//                 dominantVal = num;
//             }
//         }
//         if (n%2==1 && dominantFreq <= (n+1)/2){
//             return -1;
//         }

//         int i=0, currDominantCount = 0;
//         for (;i<n; ++i){
//             if (nums[i]==dominantVal){
//                 ++currDominantCount;
//             }

//             if (currDominantCount > (i+1)/2){
//                 break;
//             }
//         }

//         return i;
//     }
// };