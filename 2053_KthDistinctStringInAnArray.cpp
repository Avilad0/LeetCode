#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        unordered_map<string,int> freq;
        
        for (auto& s:arr){
            ++freq[s];
        }

        for (auto& s:arr){
            if (freq[s]==1) --k;

            if(k==0) return s;
        }

        return "";
    }
};