#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {

        unordered_map<int,int> remainders_freq;
        remainders_freq[0]=1;

        int i, ans =0, n = nums.size(),sum_mod=0;
        for (i=0;i<n;++i){
            // sum+=nums[i];
            
            // t=sum%k;
            // if (t<0){
            //     t+=k;
            // }
            // replaced it by below single line
            sum_mod=(sum_mod + nums[i]%k + k)%k;

            //add possible combination count to ans before incrementing
            ans+=remainders_freq[sum_mod];
            ++remainders_freq[sum_mod];
        }
        return ans;
    }
};

int main(){
    Solution s;
    // vector<int> nums = {1,2,3};
    // int k = 5;
    // cout<<-5%3;
    // vector<int> nums = {-1,2,9};
    // int k = 2;
    vector<int> nums = {2,-2,2,-4};
    int k = 6;
    cout<<s.subarraysDivByK(nums, k);
    return 0;
}


// nums =   [2,-2,2,-4] k = 6
// sum      [2, 0,2,-2]
// %        [2, 0,2, 2]
//output = 4 [actual ans=2]

//     -5, 5
// sum -5  0
// %    2  0
// output =1

// Input: 
// nums = [4,5,0,-2,-3,1], k = 5
// sum  = [4,9,9, 7, 4,5]
// %    = [1,1,1, 2, 1,0]
// [rem 0: count 2]= +(1)
// [rem 1: count 4]= +(1+2+3)         
// Output: 7


// k = 9
// nums = 1 2 3  5  5  6  7  8  9
// sum  = 1 3 6 11 16 22 29 37 46
// %    = 1 3 6  2  7  4  2  1  1


// nums = [23,  2,  6,  4,  7], k = 6
// sum  = [23, 25, 31, 35, 42]
// %    = [ 5,  1,  1,  5,  0]
