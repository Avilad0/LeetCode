#include<bits/stdc++.h>
using namespace std;

// Line-Sweep algo, TC - O(N+M), SC - O(N)
class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n=nums.size(), m=queries.size(), k=-1, sum=0;
        vector<int> diff(n+1,0);

        for (int i=0;i<n;++i){
            while (sum+diff[i]<nums[i]){
                k++;
                if (k==m)   return -1;
                
                auto &left = queries[k][0], &right = queries[k][1], &val = queries[k][2];
                if (right>=i){
                    diff[max(i,left) ] += val;
                    diff[right+1]-=val;
                }
            }
            sum+=diff[i];
        }

        return k+1;
    }
};

// // binary search, TC - O(log(M)⋅(N+M)), SC - O(N)
// class Solution {
// private:
//     bool check(vector<int>& nums, vector<vector<int>>& queries, int& n, int& k){
//         vector<int> diff(n, 0);
//         for(int i=0;i<k;++i){
//             diff[queries[i][0]] += queries[i][2];
//             if(queries[i][1] < n-1)  diff[queries[i][1]+1] -= queries[i][2];
//         }

//         int sum = 0;
//         for (int i=0;i<n;++i){
//             sum += diff[i];
//             if (nums[i]>sum)    return false;
//         }

//         return true;
//     }

// public:
//     int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
//         int n=nums.size(), left=0, right=queries.size(), mid, ans=-1;

//         while (left<=right){
//             mid = (left+right)>>1;
//             if (check(nums, queries, n, mid)){
//                 ans = mid;
//                 right = mid-1;
//             } else {
//                 left = mid+1;
//             }
//         }

//         return ans;
//     }
// };

int main(){
    Solution s;
    vector<int> nums = {5};
    vector<vector<int>> queries = {{0,0,5},{0,0,1},{0,0,3},{0,0,2}};
    cout << s.minZeroArray(nums, queries) << endl;
    return 0;
}