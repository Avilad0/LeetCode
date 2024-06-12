#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int freq[3]={0,0,0},i,j,k=0;
        for (auto& n:nums){
            ++freq[n];
        }

        for (i=0;i<3;++i){
            for (j=0;j<freq[i];++j,++k){
                nums[k]=i;
            }
        }
    }
};