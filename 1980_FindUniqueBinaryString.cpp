#include<bits/stdc++.h>
using namespace std;

// since nums.size == nums[0].size, we can use 1 bit from each position and negate it.
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        int n = nums.size();
        string ans(n, '0');
        for (int i=0;i<n; ++i){
            if (nums[i][i]=='0')    ans[i]='1';
        }

        return ans;
    }
};

// If nums.size != nums[0].size, then use this approach
// class Solution {
// public:
//     string findDifferentBinaryString(vector<string>& nums) {
//         unordered_set<int> numsSet;
//         for (string& num: nums) numsSet.insert(stoi(num,0,2));
        
//         int n = nums[0].size(), range=1<<n;
//         for (int i=0;i<range; ++i){
//             if (numsSet.find(i)==numsSet.end()) return bitset<16>(i).to_string().substr(16-n);
//         }

//         return "";
//     }
// };