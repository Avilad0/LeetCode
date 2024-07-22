#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<int> indices(names.size());
        iota(indices.begin(), indices.end(), 0);
        sort(indices.begin(), indices.end(),
           [&](int a, int b) -> bool {
                return heights[a] > heights[b];
            });

        vector<string> ans(names.size());
        for (int i =0; i<names.size();++i){
            ans[i]=names[indices[i]];
        }

        return ans;
    }
};