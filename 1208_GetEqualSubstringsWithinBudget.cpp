#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int n= s.length();
        int ans = 0, running_cost = 0,j=0;

        for (int i=0;i<n;++i){
            running_cost+=abs(s[i]-t[i]);

            while(running_cost>maxCost){
                running_cost-=abs(s[j]-t[j]);
                ++j;
            }

            if (i-j+1 > ans){
                ans = i-j+1;
            }
        }
        
        return ans;
    }
};


// class Solution {
// public:
//     int equalSubstring(string s, string t, int maxCost) {
//         int n= s.length();
        
//         int ans = 0;
//         int running_cost = 0;
//         int i=0, j=0, count = 0 , x;        
//         while (i<n){
//             x= abs(s[j]-t[j]);
//             while (j<n && (running_cost+x)<=maxCost){
//                 running_cost+=x;
//                 ++j;
//                 ++count;
//                 x= abs(s[j]-t[j]);
//             }

//             if (count>ans){
//                 ans = count; 
//             }
//             if (j==n-1 && j-i+1<=ans){
//                 break;
//             }
//             running_cost-=abs(s[i]-t[i]);
//             ++i;
//             --count;
//         }

//         return ans;
//     }
// };

int main(){
    Solution s;
    cout<<s.equalSubstring("thjdoffka","qhrnlntls",11);
    return 0;
}