#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        unordered_set<int> numsSet;
        for (string& num: nums) numsSet.insert(stoi(num,0,2));
        
        int n = nums[0].size(), range=1<<n;
        for (int i=0;i<range; ++i){
            if (numsSet.find(i)==numsSet.end()) return bitset<16>(i).to_string().substr(16-n);
        }

        return "";
    }
};

// class Solution {
// public:
//     string findDifferentBinaryString(vector<string>& nums) {
//         string ans;
//         int m=nums.size(), n= nums[0].size(), i, j, count;
//         for (j=0;j<n; ++j){
//             count = 0;
//             for (i=0;i<m;++i){
//                 if (nums[i][j]=='1') count++;
//             }
//             if (count<n){
//                 ans.push_back('1');
//             } else{
//                 ans.push_back('0');
//             }
//         }
//         return ans;
//     }
// };