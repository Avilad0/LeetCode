#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    // fastest - O(n)
    int longestSubarray(vector<int>& nums, int limit) {
        int n = nums.size();
        if (n<2){
            return n;
        }

        deque<int> maxQueue = {nums[0]}, minQueue = {nums[0]};
        int ans =1, i=0,j=1,t;

        for (j=1;j<n;++j){
            
            while ( !maxQueue.empty() && maxQueue.back()<nums[j]){
                maxQueue.pop_back();
            }
            maxQueue.push_back(nums[j]);

            while ( !minQueue.empty() && minQueue.back()>nums[j]){
                minQueue.pop_back();
            }
            minQueue.push_back(nums[j]);

            while(maxQueue.front() - minQueue.front() >limit){
                if (maxQueue.front() == nums[i]) {
                    maxQueue.pop_front();
                }
                if (minQueue.front() == nums[i]) {
                    minQueue.pop_front();
                }
                ++i;
            }

            if ( j-i+1 >ans){
                ans = j-i+1;
            }
        }

        return ans;
    }
};

int main(){
    Solution s;
    // vector<int> nums = {1,5,6,7,8,10,6,5,6};
    // int limit = 4;  //Output =  5

    vector<int> nums = {8,2,4,7};
    int limit = 4;  //Output =  2

    cout<<s.longestSubarray(nums, limit);
    return 0;
}

    // // slower but stil - nlogn 
    // int longestSubarray(vector<int>& nums, int limit) {
    //     int n = nums.size();
    //     if (n<2){
    //         return n;
    //     }

    //     multiset<int> sortedNums = {nums[0]};
    //     int ans =1, i=0,j=1,t;

    //     for (j=1;j<n;++j){
    //         sortedNums.insert(nums[j]);

    //         while ( *sortedNums.rbegin() - *sortedNums.begin() >limit){
    //             sortedNums.erase(sortedNums.find(nums[i]));
    //             ++i;

    //         }

    //         if ( j-i+1 >ans){
    //             ans = j-i+1;
    //         }
    //     }

    //     return ans;
    // }

    // // slowest - nlogn
    // int longestSubarray(vector<int>& nums, int limit) {
    //     int n = nums.size();
    //     if (n<2){
    //         return n;
    //     }

    //     vector<int> sortedNums = {nums[0]};
    //     int ans =1, i=0,j=1,t;

    //     while (j<n){
            
    //         if (nums[j]<=sortedNums[0]){
    //             while ( !sortedNums.empty() &&  *sortedNums.rbegin() - nums[j] >limit){
    //                 sortedNums.erase(find(sortedNums.begin(), sortedNums.end(), nums[i]));
    //                 ++i;
    //             }
            
    //             sortedNums.insert(sortedNums.begin(), nums[j]);
    //         } else if (nums[j] >= *sortedNums.rbegin()){
        
    //             while (!sortedNums.empty() &&   nums[j] - sortedNums[0] >limit){
    //                 sortedNums.erase(find(sortedNums.begin(), sortedNums.end(), nums[i]));
    //                 ++i;
    //             }
            
    //             sortedNums.insert(sortedNums.end(), nums[j]);
    //         } else {
    //             for (t=1; sortedNums[t]<nums[j];++t);

    //             sortedNums.insert(sortedNums.begin()+t, nums[j]);
    //         }

    //         ++j;
    //         if ( j-i>ans){
    //             ans = j-i;
    //         }
    //     }

    //     return ans;
    // }