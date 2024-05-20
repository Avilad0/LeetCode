#include<bits/stdc++.h>
using namespace std;

class Solution {
public:

    //both codes are correct

    int subsetXORSum(vector<int>& nums) {
        int ans = 0;
        for(int n: nums){
            ans|=n;
        }
        return ans<<(nums.size()-1);
    }


    // int subsetXORSum(vector<int>& nums) {
    //     return getXOR(nums, nums.size(), 0, 0);
    // }

    // int getXOR(vector<int>& nums, int n, int i, int running_ans) {
    //     if (i==n){
    //         return running_ans; 
    //     }
    //     return getXOR(nums,n,i+1, running_ans^nums[i]) + getXOR(nums,n,i+1, running_ans);

    // }

};