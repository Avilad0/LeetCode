#include<bits/stdc++.h>
using namespace std;

// with O(1) space
class Solution {
public:
    long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
        
        long long maxVal = 0;
        int n = nums.size(), toBeIncreasedCount = 0, minDifference = INT_MAX;

        for (int node=0;node<n;++node){
            if ((nums[node]^k)>nums[node]){
                maxVal += (nums[node]^k);
                minDifference = min (minDifference, (nums[node]^k) - nums[node]);
                ++toBeIncreasedCount;
            } else {
                maxVal += (nums[node]);
                minDifference = min (minDifference, nums[node] - (nums[node]^k));            
            }
        }
        
        if (toBeIncreasedCount&1){
            maxVal -= minDifference;
        }

        return maxVal;
    }
};


// // with O(n) space
// class Solution {
// public:
//     long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
//         int n = nums.size();

//         vector<int> nodesToIncrease, alreadyMaxNodes;
//         for (int node=0;node<n;++node){
//             if ((nums[node]^k)>nums[node]){
//                 nodesToIncrease.push_back(node);
//             } else {
//                 alreadyMaxNodes.push_back(node);
//             }
//         }
        
//         long long maxVal = 0;
//         if (nodesToIncrease.size()%2==0){
//             for (auto& node: nodesToIncrease)  maxVal += (nums[node]^k);
//             for (auto& node: alreadyMaxNodes)  maxVal += (nums[node]);
//         } else {

//             int minDifference = INT_MAX; 
//             for (int i=0; i<nodesToIncrease.size(); ++i) {
//                 maxVal += (nums[nodesToIncrease[i]]^k);
//                 minDifference = min (minDifference, (nums[nodesToIncrease[i]]^k) - nums[nodesToIncrease[i]]);
//             }

//             for (int i=0; i<alreadyMaxNodes.size(); ++i){
//                 maxVal += nums[alreadyMaxNodes[i]];
//                 minDifference = min(minDifference, nums[alreadyMaxNodes[i]] - (nums[alreadyMaxNodes[i]]^k));
//             }

//             maxVal -= minDifference;
//         }

//         return maxVal;
//     }
// };

int main(){
    Solution s;
    // vector<int> nums{1,2,1};
    // vector<vector<int>> edges = {{0,1},{0,2}};
    // int k = 3;
    // cout<<s.maximumValueSum(nums, k, edges); // 6

    vector<int> nums{24,78,1,97,44};
    vector<vector<int>> edges = {{0,2},{1,2},{4,2},{3,4}};
    int k = 6;
    cout<<s.maximumValueSum(nums, k, edges); // 260
    return 0;
}

/*
24 = 0011000 , 0011110 = 30 
78 = 1001110 , 1001000 = 72
1  = 0000001 , 0000111 =  7
97 = 1100001 , 1100111 =103
44 = 0101100 , 0101010 = 42 

ans = 30 + 78 + 7 + 103 + 42 = 260

0 -- 2 -- 1
     |
     4 -- 3
*/