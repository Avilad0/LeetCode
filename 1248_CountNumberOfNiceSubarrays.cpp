#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        int leftCount=0, left=0, right=0, n = nums.size(), ans=0;

        for(;right<n;++right){
            k-= nums[right]%2;

            if (k==0){
                leftCount=0;
                while (k==0){
                    k+= nums[left]%2;
                    ++left;
                    ++leftCount;
                }
            }
            ans+=leftCount;
        }

        return ans;
    }
};

// class Solution {
// public:
//     int numberOfSubarrays(vector<int>& nums, int k) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

//         int leftCount=1, rightCount=1, left=0, right, n = nums.size(), ans;
        
//         while ( left<n && nums[left]%2==0){
//             ++left;
//             ++leftCount;
//         }
        
//         if(left==n){
//             return 0;
//         }

//         right = left + 1;
//         --k;
//         while ( right<n && k>0){
//             if (nums[right]%2==1){
//                 --k;
//             }
//             ++right;
//         }

//         if (k!=0){
//             return 0;
//         }

//         while ( right<n && nums[right]%2==0){
//             ++rightCount;
//             ++right;
//         }

//         ans = leftCount*rightCount;

//         while(right<n){
//             leftCount=1;
//             ++left;
//             while (nums[left]%2==0){
//                 ++left;
//                 ++leftCount;
//             }

//             rightCount=1;
//             ++right;
//             while(right<n && nums[right]%2==0){
//                 ++right;
//                 ++rightCount;
//             }

//             ans+= leftCount*rightCount;
//         }

//         return ans;

//     }
// };

int main(){
    Solution s;
    // vector<int> nums = {2,2,2,1,2,2,1,2,2,2};
    // int k = 2;

    vector<int> nums = {1,1,2,1,1};
    int k = 3;
    cout<<s.numberOfSubarrays(nums,k);
    return 0;
}


// Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
// Output: 16

// 2,2,2,1,2,2,1,2,2,2
// -     -     -     -

// 4*4 = 16


// Input: nums = [1,1,2,1,1], k = 3
// Output: 2

// 1,1,2,1,1
// -     -
//   -     -
// 1*1 + 1*1 = 2


// k=2
// 2,2,2,1,2,2,1,2,2,2,1,2,2,2
// l l l l
//         r r r
//               r r r
//         l l l 
//                     r r r r
// 
// 
// 16 + 12 = 28