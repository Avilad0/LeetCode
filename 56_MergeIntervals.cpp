#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> mergedInvervals;

        for (auto& interval: intervals){
            if (mergedInvervals.empty() || mergedInvervals.back()[1]< interval[0]){
                mergedInvervals.emplace_back(interval);
            } else {
                mergedInvervals.back()[1] = max(mergedInvervals.back()[1], interval[1]);
            }
        }

        return mergedInvervals;
    }
};