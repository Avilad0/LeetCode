#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long maxVal = 0;
        
        int n = nums.size(), maxNum=0, maxDiff=0;
        for (int k=0; k<n; ++k){
            maxVal = max(maxVal, (long long) maxDiff *nums[k]);
            maxDiff = max(maxDiff, maxNum - nums[k]);
            maxNum = max(maxNum, nums[k]);
        }

        return maxVal;
    }
};