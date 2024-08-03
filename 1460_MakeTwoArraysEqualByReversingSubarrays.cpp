#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        unordered_map<int,int> freq; 
        for (auto& n:arr){
            ++freq[n];
        }

        for(auto& t:target) {
            --freq[t];
            if(freq[t]<0) return false;
        }
        return true;
    }
};

// class Solution {
// public:
//     bool canBeEqual(vector<int>& target, vector<int>& arr) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
//         unordered_map<int,int> freq; 
//         for (int i=0;i<arr.size();++i){
//             ++freq[arr[i]];
//             --freq[target[i]];
//         }
//         for(auto& [n,f]: freq) if (f!=0) return false;

//         return true;
//     }
// };