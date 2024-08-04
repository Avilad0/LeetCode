#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        vector<int> sums;
        long long sum;
        int i=0,j;
        
        for(;i<n;++i){
            sum=0;
            for(j=i;j<n;++j){
                sum+=nums[j];
                sums.push_back(sum);
            }
        }

        sort(sums.begin(), sums.end());

        sum=0;
        for(i=left-1;i<right;++i)   sum= (sum+sums[i])%1000000007;

        return sum;
    }
};