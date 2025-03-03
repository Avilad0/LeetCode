#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int n= nums.size();
        vector<int> ans(n,pivot);
        
        int s=0, e=n-1;
        for (int i=0;i<n;++i){
            if(nums[i]<pivot){
                ans[s++] =nums[i];
            }
            
            if(nums[n-1-i]>pivot){
                ans[e--] = nums[n-1-i];
            }
        }
        
        return ans;
    }
};

// class Solution {
// public:
//     vector<int> pivotArray(vector<int>& nums, int pivot) {
//         int n= nums.size(), i,j;
//         vector<int> ans(n,pivot);
        
//         j=0;
//         for (i=0;i<n;++i){
//             if(nums[i]<pivot){
//                 ans[j++] =nums[i];
//             }
//         }
        
//         j=n-1;
//         for (i=n-1;i>=0;--i){
//             if(nums[i]>pivot){
//                 ans[j--] = nums[i];
//             }
//         }
        
//         return ans;
//     }
// };

int main(){
    Solution s;
    vector<int> nums = {9,12,5,10,14,3,10};
    int pivot = 10;
    vector<int> ans = s.pivotArray(nums, pivot);
    for (auto& num: ans)    cout<<num<<" ";
    return 0;
}