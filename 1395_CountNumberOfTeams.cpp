#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numTeams(vector<int>& rating) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    }
};




// // Very Slow
// class Solution {
// public:
//     int numTeams(vector<int>& rating) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
//         int ans=0, i,j,k, n = rating.size();

//         for (i=0;i<n-2;++i){
//             for (j=i+1;j<n-1;++j){
//                 for (k=j+1;k<n;++k){
//                     if ( (rating[i]<rating[j] && rating[j]<rating[k]) || (rating[i]>rating[j] && rating[j]>rating[k])) ++ans;
//                 }
//             }
//         }

//         return ans;
//     }
// };

int main(){
    Solution s;
    vector<int> rating = {2,5,3,4,1};  //Output: 3
    cout<<s.numTeams(rating);
    return 0;
}