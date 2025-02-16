#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxIncreasingGroups(vector<int>& usageLimits) {
        sort(usageLimits.begin(), usageLimits.end());
        long long total = 0, count=0;
        for (int i=0 ;i<usageLimits.size();++i){
            total+=usageLimits[i];
            if (total >= ((count+1)*(count+2))/2){
                ++count;
            }
        }
        return count;
    }
};


// logic explanation: https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/solutions/3803590/simple-python-math-solution-o-nlogn-time-complexity-only-7-lines-of-code/