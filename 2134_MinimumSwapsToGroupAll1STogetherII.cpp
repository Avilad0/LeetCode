#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minSwaps(vector<int>& nums) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        int n=nums.size(), totalOnes =0, zeros=0, minimumSwaps, i;
        
        for (auto& num:nums) if (num==1) ++totalOnes;

        if (totalOnes==0 || totalOnes==1 || totalOnes==n || totalOnes == n-1) return 0;

        for (i=0;i<totalOnes;++i) if (nums[i]==0) ++zeros;

        minimumSwaps=zeros;

        for(i=0;i<n;++i){
            if(nums[i]==0) --zeros;
            if (nums[(i+totalOnes)%n]==0) ++zeros;

            minimumSwaps = min(minimumSwaps, zeros);
        }

        return minimumSwaps;
    }
};



// nums = [1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0] // output=7
// zerosSubsetCounts= [2,1,3,2,2,4,2,2]   1s=16