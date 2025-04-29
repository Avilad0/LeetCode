#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        long long count = 0;
        int n=nums.size(), maxNum = *max_element(nums.begin(), nums.end()), maxCount = 0, left = 0;
        
        for (int right=0; right<n; ++right){
            if (nums[right]==maxNum) ++maxCount;

            while (maxCount>=k){
                count+=n-right;
                if (nums[left]==maxNum) --maxCount;
                ++left;
            }
        }

        return count;
    }
};