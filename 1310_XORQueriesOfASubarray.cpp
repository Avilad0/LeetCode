#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);      

        int n = arr.size()+1, nq = queries.size(), i;
        vector<int> ans(nq), xors(n,0);

        for (i=1;i<n; ++i) xors[i]=xors[i-1]^arr[i-1];

        for (i=0;i<nq;++i)  ans[i] = xors[queries[i][0]] ^ xors[queries[i][1]+1];

        return ans;
    }
};