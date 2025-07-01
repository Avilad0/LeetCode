#include<bits/stdc++.h>
using namespace std;

// tc = O(n**2)
class Solution {
    public:
    int numTeams(vector<int>& rating) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        int n = rating.size(), ans = 0;
        
        for (int i = 1; i<n-1; ++i){
            int lessThanOnLeft = 0 , lessThanOnRight = 0, greaterThanOnLeft = 0, greaterThanOnRight = 0;
            for (int j=0; j<i; ++j){
                if (rating[i]<rating[j]) ++greaterThanOnLeft;
                else if (rating[i]>rating[j]) ++lessThanOnLeft;
            }
            
            for (int j=i+1; j<n; ++j){
                if (rating[i]<rating[j]) ++greaterThanOnRight;
                else if (rating[i]>rating[j]) ++lessThanOnRight;
            }

            ans += lessThanOnLeft*greaterThanOnRight + greaterThanOnLeft*lessThanOnRight;
        }

        return ans;
    }
};




// // Very Slow, tc = O(n**3)
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