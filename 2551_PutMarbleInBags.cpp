#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        int n = weights.size();
        
        vector<int> pairWeights;
        for (int i=0;i<n-1; ++i){
            pairWeights.emplace_back(weights[i]+weights[i+1]);
        }
        sort(pairWeights.begin(), pairWeights.end());

        long long difference = 0;
        for (int i=0 ;i<k-1;++i){
            difference += pairWeights[n-i-2] - pairWeights[i];
        }

        return difference;
    }
};