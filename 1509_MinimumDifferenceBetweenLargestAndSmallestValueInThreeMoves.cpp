#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n = nums.size();

        if (n<5) return 0;

        partial_sort(nums.begin(), nums.begin() + 4, nums.end());
        
        nth_element(nums.begin() + 4, nums.begin() + (n - 4), nums.end());

        sort(nums.begin() + (n - 4), nums.end());


        long long minDiff = nums[n-1]- nums[0];
        for (int i=0;i<=3;++i){
            if (nums[n-1-i]-nums[3-i] <  minDiff){
                minDiff = nums[n-1-i]-nums[3-i];
            }
        }
        return minDiff;
    }
};



    // int minDifference(vector<int>& nums) {
    //     int n = nums.size();

    //     if (n<5) return 0;

    //     sort(nums.begin(), nums.end());
    //     long long minDiff = nums[n-1]- nums[0];
    //     for (int i=0;i<=3;++i){
    //         if (nums[n-1-i]-nums[3-i] <  minDiff){
    //             minDiff = nums[n-1-i]-nums[3-i];
    //         }
    //     }

    //     return minDiff;
    // }


// 1 3 5 6 8 10 12 15 18 19
// l                      r
