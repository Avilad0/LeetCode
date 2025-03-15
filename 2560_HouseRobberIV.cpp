#include<bits/stdc++.h>
using namespace std;

class Solution {
private:
    bool isPossible(vector<int>& nums, int k, int mid){
        int n= nums.size(), i, j, count=0;
        for(i=0; i<n; i++){
            if (nums[i]<=mid){
                ++count;
                ++i;
            }
        }
        return count>=k;
    }
public:
    int minCapability(vector<int>& nums, int k) {
        int n= nums.size(), left=nums[0], right=nums[0], mid, ans;
        for(int i=1; i<n;++i){
            if (nums[i]<left) left=nums[i];
            else if (nums[i]>right) right=nums[i];
        }
        
        ans = right;
        while(left<=right){
            mid = (left+right)/2;
            if (isPossible(nums, k, mid)){
                ans = mid;
                right= mid-1;
            } else {
                left = mid+1;
            }
        }

        return ans;
    }
};


/*
Input: nums = [2,7,9,3,1], k = 2
Output: 2

*/