#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n=nums.size(), ans =0, i;
        for (i=0; i< (n-2); ++i){
            if (nums[i]==1) continue;

            ++ans;
            nums[i+1] = !nums[i+1];
            nums[i+2] = !nums[i+2];
        }

        if (nums[n-2]==0 || nums[n-1]==0) return -1; 

        return ans;
    }
};



// without inplace modification for input array.
// class Solution {
// public:
//     int minOperations(vector<int>& nums) {
//         int n=nums.size(), ans =0, i;
//         vector<int> temp = {nums[0], nums[1], nums[2]};
//         for (i=3; i<n; ++i){
//             if (temp[0]==1){
//                 temp[0] = temp[1];
//                 temp[1] = temp[2];
//             } else {
//                 ++ans;
//                 temp[0] = !temp[1];
//                 temp[1] = !temp[2];
//             }
//             temp[2] = nums[i];
//         }

//         int sumTemp = temp[0]+temp[1]+temp[2];
//         if (sumTemp==3) return ans; 
//         if (sumTemp==0) return ans+1;

//         return -1;
//     }
// };