#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {

        vector<int> freq(n,0);

        for (auto& r:roads){
            ++freq[r[0]];
            ++freq[r[1]];
        }

        sort(freq.begin(), freq.end());

        long long ans =0;
        for (long long i=1;i<=n;++i){
            ans+= (i*freq[i-1]);
        }

        return ans;
    }
};