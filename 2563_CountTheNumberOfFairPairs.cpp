#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        return count(nums, upper) - count(nums, lower-1);
    }

    long long count(vector<int>& nums, int limit){
        long long ans = 0;
        int left=0;
        for (int right=nums.size()-1;right>left; --right){
            while (left<right && nums[left]+nums[right]<=limit){
                left++;
            }
            ans+=left;
            if (left==right) --left;
        }
        return ans;
    }

};