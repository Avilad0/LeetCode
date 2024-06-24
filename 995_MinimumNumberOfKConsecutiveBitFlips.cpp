#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int n = nums.size(), flipped = 0, ans = 0;
        deque<int> flipQueue;

        for (int i = 0; i < n; ++i) {
            if (i >= k) {
                flipped ^= flipQueue.front();
                flipQueue.pop_front();
            }

            if (flipped == nums[i]) {
                if (i + k > n) {
                    return -1;
                }
                flipQueue.push_back(1);
                flipped ^= 1;
                ans += 1;
            } else {
                flipQueue.push_back(0);
            }
        }

        return ans;
    }
};



// k=3
// 0 1 0 1 0 1        ans
// 1 0 1 1 0 1         1
// 1 1 0 0 0 1         2
// 1 1 1 1 1 1         3

// k=2
// 0 1 0 1 0 1        ans
// 1 0 0 1 0 1        1
// 1 1 1 1 0 1        2
// 1 1 1 1 1 0        3
//                    -1



// k=3
// 1 0 1 0 0 0 1 0       ans       1 0 1 0 0 0 1 0  
// 1 1 0 1 0 0 1 0         1       
// 1 1 1 0 1 0 1 0         2       
// 1 1 1 1 0 1 1 0         3       1 1 1 1 0 1 1 0
// 1 1 1 1 1 0 0 0         4
// 1 1 1 1 1 1 1 1         5

// 1 1 1 1 0   ,k=2
// output = -1;


// nums = [0,0,0,1,0,1,1,0], k = 3
//         1,1,1,1,0,1,1,0
//         1,1,1,1,1,0,0,0
//         1,1,1,1,1,1,1,1
// Output: 3

// nums = [0,0,0,1,0,1,1,1], k = 3
//         1,1,1,1,0,1,1,1
//         1,1,1,1,1,0,0,1
//         1,1,1,1,1,1,1,0
// Output: -1



    // TLE in very large cases
    // int minKBitFlips(vector<int>& nums, int k) {
    //     int ans=0, i=0, j, n = nums.size();
        
    //     for (;i<=n-k; ++i){
    //         if (nums[i]==1){
    //             continue;
    //         }
    //         for (j=i; j<i+k;++j){
    //             nums[j]^=1;
    //         }
    //         ++ans;
    //     }

    //     for (;i<n;++i){
    //         if (nums[i]==0){
    //             return -1;
    //         }
    //     }

    //     return ans;
    // }

