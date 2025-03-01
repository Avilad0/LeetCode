#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n=nums.size(), i=0;
        for(int j=0; j<n; ++j){
            if (j<n-1 && nums[j]==nums[j+1]){
                nums[j]*=2;
                nums[j+1]=0;
            }
            if (nums[j]!=0){
                if (i!=j){
                    nums[i]=nums[j];
                    nums[j]=0;
                }
                ++i;
            }
        }

        return nums;
    }
};

// class Solution {
// public:
//     vector<int> applyOperations(vector<int>& nums) {
//         int n=nums.size(), i=0, j=0;
//         while (j<n){
//             if (nums[j]==0) {
//                 j++;
//             } else if (j==n-1 || nums[j]!=nums[j+1]){
//                 nums[i++] = nums[j];
//                 j++;
//             } else {
//                 nums[i++] = nums[j]*2;
//                 j+=2;
//             }
//         }

//         while (i<n) nums[i++] = 0;

//         return nums;
//     }
// };