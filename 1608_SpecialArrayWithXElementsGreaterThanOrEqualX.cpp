#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int specialArray(vector<int>& nums) {
        int n = nums.size();

        sort(nums.begin(), nums.end());

        for (int i=0;i<n;i++){
            if(n-i<=nums[i])
            {   
                if (i==0 || (n-i)>nums[i-1])
                    return n-i;
                else
                    return -1;
            }
        }

        return -1;
    }
};