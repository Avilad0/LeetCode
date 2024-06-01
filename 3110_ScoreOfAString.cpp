#include<bits/stdc++.h>
using namespace std;


// class Solution {
// public:
//     int scoreOfString(string s) {
//         int ans=0, t=0;
//         for (int i=1;i<s.length();++i){
//             t= s[i]-s[i-1];
//             if (t>0){
//                 ans+=t;
//             } else{
//                 ans-=t;
//             }
//         }
//         return ans;
//     }
// };

class Solution {
public:
    int scoreOfString(string s) {
        int ans=0;
        for (int i=1;i<s.length();++i){
            ans+=abs(s[i]-s[i-1]);
        }
        return ans;
    }
};