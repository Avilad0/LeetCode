#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();
        long long maxValue = 0;
        for (int i=0; i<n-2; ++i){
            for (int j=i+1; j<n-1; ++j){
                for (int k=j+1; k<n; ++k){
                    if (( (long long)nums[i] - nums[j])*nums[k] > maxValue){
                        maxValue = ((long long)nums[i] - nums[j])*nums[k];
                    }
                }
            }
        }

        return maxValue;
    }
};
    //     int n=nums.size(), i=0;
        
    //     while (i<n && nums[i+1]>=nums[i]) ++i;

    //     if (i==n)   return 0;

    //     int j = i+1 , iMinusJ = nums[i]-nums[j];
    //     for(int index=j+1; index<n; ++index){
    //         if (nums[index]>nums[i]){
    //             i=index;
    //             j=-1;
    //             k=-1;
    //         }
    //         if (nums[index] < nums[j]){
    //             j=index;
    //             iMinusJ = nums[i]-nums[j];
    //         }
    //     }
    // }
// };