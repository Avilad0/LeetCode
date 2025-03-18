#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int n = nums.size(), ans = 1, right=0, left=0, setBits = 0;
        
        for(;right<n;++right){
            
            while (setBits & nums[right] != 0){
                setBits ^= nums[left];
                ++left;
            }

            setBits |= nums[right];
            if (ans < right-left+1) ans = right-left+1;
        }

        return ans;
    }
};


// class Solution {
// public:
//     int longestNiceSubarray(vector<int>& nums) {
//         vector<bool> setBits(32, false), setTemp;
//         int n = nums.size(), ans = 1, right=0, left=0, num, bit;
//         bool isNice;
        
//         for(;right<n;++right){
//             num = nums[right];
//             setTemp.assign(32, false);
//             bit=0;
//             isNice = true;
//             while (num){
//                 if (num&1) {
//                     if (setBits[bit]) {
//                         isNice = false;
//                         break;
//                     }
//                     setTemp[bit] = true;
//                 }
//                 num >>= 1;
//                 ++bit;
//             }

//             if (isNice) {
//                 ans = max(ans, right-left+1);
//                 for (;bit>=0; --bit){
//                     setBits[bit] = setBits[bit] || setTemp[bit];
//                 }
//             } else {
//                 for (bit=0;bit<32; ++bit)
//                     if ((1<<bit) & nums[left]) 
//                         setBits[bit] = false;

//                 left++;
//                 right--;
//             }
//         }

//         return ans;
//     }
// };

main(){
    Solution s;
    vector<int> nums = {1,3,8,48,10};   // 3
    cout<<s.longestNiceSubarray(nums)<<endl;
}

/*
[1,3,8,48,10]
*/