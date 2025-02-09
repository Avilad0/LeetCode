#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        unordered_map<int,int> combFreq;
        long long goodCount = 0, n = nums.size();
        for (int i=0;i<n;++i){
            goodCount+=combFreq[i-nums[i]];
            combFreq[i-nums[i]]++;
        }

        return (n*(n-1)/2) - goodCount;
    }
};

// class Solution {
// public:
//     long long countBadPairs(vector<int>& nums) {
//         unordered_map<int,int> combFreq;
//         long long goodCount = 0, n = nums.size();
//         for (int i=0;i<n;++i){
//             if (combFreq.find(i-nums[i]) != combFreq.end()){
//                 goodCount+=combFreq[i-nums[i]];
//                 combFreq[i-nums[i]]++;
//             } else {
//                 combFreq[i-nums[i]] = 1;
//             }
//         }

//         return (n*(n-1)/2) - goodCount;
//     }
// };



/*
Input: nums = [4,1,3,3]
Output: 5

bad = i<j, j-i!=nums[j]-nums[i]
good = i<j, j-i==nums[j]-nums[i]
            j-i - (nums[j]-nums[i]) == 0
            (j-nums[j]) == (i-nums[i])


total pairs for 4 = 1+2+3 = (n-1)n/2

*/