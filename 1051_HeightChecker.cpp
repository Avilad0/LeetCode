#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> sorted_heights(heights);
        sort(sorted_heights.begin(), sorted_heights.end());
        int ans=0;
        for (int i=0;i<heights.size();++i){
            if (heights[i]!=sorted_heights[i]){
                ++ans;
            }
        }
        return ans;
        
    }
};