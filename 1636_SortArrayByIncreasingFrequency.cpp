#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int, int> freq;
        for (auto& n : nums) freq[n]++;

        sort(nums.begin(), nums.end(), [&](int a, int b) {
            if (freq[a] == freq[b]) {
                return a > b;
            }
            return freq[a] < freq[b];
        });

        return nums;
    }
};

// class Solution {
// public:
//     vector<int> frequencySort(vector<int>& nums) {
//         unordered_map<int,int> freq;
//         for (auto& n: nums) freq[n]++;

//         map<int, priority_queue<int>> freqToNums;
//         for (auto& [n,f]: freq){
//             freqToNums[f].push(n);
//         }

//         int i=0,j;
//         for (auto& [f,nq]: freqToNums){
//             while (!nq.empty()){
//                 for (j=0 ; j<f;++j){
//                     nums[i+j] = nq.top();
//                 }
//                 i+=f;
//                 nq.pop();
//             }
//         }

//         return nums;
//     }
// };