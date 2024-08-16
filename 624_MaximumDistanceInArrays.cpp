#include<bits/stdc++.h>
using namespace std;

//both codes beats more than 99%

class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        int minn=arrays[0][0], maxx=arrays[0][arrays[0].size()-1], diff=0, i=1, m=arrays.size(), currMin, currMax;

        for (;i<m;++i){
            currMin = arrays[i][0];
            currMax = arrays[i][arrays[i].size()-1];

            diff = max(diff, max(currMax-minn, maxx-currMin));
            minn = min(minn, currMin);
            maxx = max(maxx, currMax);
        }

        return diff;
    }
};

// class Solution {
// public:
//     int maxDistance(vector<vector<int>>& arrays) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
//         int min1=0, min2=1, max1=0, max2=1, i=2, m=arrays.size();

//         if (arrays[0][0]>arrays[1][0]){
//             min1 = 1;
//             min2 = 0;
//         }

//         if (arrays[0][arrays[0].size()-1]<arrays[1][arrays[1].size()-1]){
//             max1 = 1;
//             max2 = 0;
//         }

//         for (;i<m;++i){
//             if (arrays[i][0]<arrays[min1][0]){
//                 min2=min1;
//                 min1=i;
//             } else if(arrays[i][0]<arrays[min2][0]) {
//                 min2=i;
//             }

//             if (arrays[i][arrays[i].size()-1] > arrays[max1][arrays[max1].size()-1]){
//                 max2=max1;
//                 max1=i;
//             } else if(arrays[i][arrays[i].size()-1] > arrays[max2][arrays[max2].size()-1]) {
//                 max2=i;
//             }
//         }

//         if (min1 != max1) return arrays[max1][arrays[max1].size()-1] - arrays[min1][0];

//         int ans1 = min1!=max2 ? arrays[max2][arrays[max2].size()-1] - arrays[min1][0] : 0;
//         int ans2 = min2!=max1 ? arrays[max1][arrays[max1].size()-1] - arrays[min2][0] : 0;

//         return max(ans1, ans2);
//     }
// };


int main(){
    Solution s;
    vector<vector<int>> arrays = {{1,2,3},{4,5},{1,2,3}};
    cout<<s.maxDistance(arrays);
    return 0;
}