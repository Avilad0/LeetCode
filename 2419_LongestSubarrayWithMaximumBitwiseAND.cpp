#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        int maxNumber=0, maxLength = 1, n= nums.size(), i=0, runningLength, curr;

        while (i<n){
            curr = nums[i++];
            runningLength=1;
            while (i<n && nums[i]==curr){
                ++runningLength;
                ++i;
            }
            if (maxNumber<curr){
                maxLength = runningLength;
                maxNumber= curr;
            } else if (maxNumber==curr){
                maxLength = max(maxLength, runningLength);
            }
        }
        return maxLength;
    }
};

int main(){
    Solution s;
    vector<int> nums = {100,5,5};
    cout<<s.longestSubarray(nums);
    return 0;
}