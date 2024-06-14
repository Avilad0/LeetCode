#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        
        sort(nums.begin(), nums.end());
        int ans =0,i,t;
        for (i=1;i<nums.size();++i){
            if (nums[i]<=nums[i-1]){
                t=nums[i-1] - nums[i] + 1;
                ans+=t;
                nums[i]+=t;
            }
        }

        return ans;
    }
};

int main(){
    Solution s;
    vector<int> numss = {3,2,1,2,1,7};
    cout<<s.minIncrementForUnique(numss);
    return 0;
}


// both approach tle

    // int minIncrementForUnique(vector<int>& nums) {
        
    //     map<int,int> nums_freq;
        
    //     for (auto& num:nums){
    //         ++nums_freq[num];
    //     }

    //     int ans =0,t;
    //     for (auto& [num,freq] : nums_freq){
    //         t=num+1;
    //         while (freq!=1){
    //             if (nums_freq.find(t)==nums_freq.end()){
    //                 ans+=t-num;
    //                 --freq;
    //                 nums_freq[t]=1;
    //             }
    //             ++t;
    //         }
    //     }
    //     return ans;
    // }



    // int minIncrementForUnique(vector<int>& nums) {
    //     sort(nums.begin(), nums.end());
    //     unordered_set<int> unique_nums;
    //     int ans =0,counter;
    //     for (auto& num:nums){
    //         counter=0;
    //         while ( unique_nums.find(num+counter)!=unique_nums.end()){
    //             counter++;
    //         }

    //         ans+=counter;
    //         unique_nums.insert(num+counter);
    //     }

    //     return ans;
    // }