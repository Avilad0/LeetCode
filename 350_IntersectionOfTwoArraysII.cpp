#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        cout.tie(nullptr);
        vector<int> intersect;
        unordered_map<int,int> freqNums1;

        for (auto& n: nums1){
            ++freqNums1[n];
        }

        for (auto& n: nums2){
            if (freqNums1[n]>0 ){
                intersect.push_back(n);
                --freqNums1[n];
            }
        }

        return intersect;
    }
};