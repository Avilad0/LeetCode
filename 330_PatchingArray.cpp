#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        long long sum = 0;
        int ans=0,i=0, l=nums.size();

        while(sum<n){
            if (i<l && nums[i]<=sum+1){
                sum+=nums[i];
                ++i;
            } else {
                ans+=1;
                sum+=sum+1;
            }
        }

        return ans;

    }
};