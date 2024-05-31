#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        int ans = 0;
        for (int& n:nums) ans^=n;
        return ans;
    }
};