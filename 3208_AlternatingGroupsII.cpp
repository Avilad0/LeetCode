#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int n=colors.size(), ans=0, prefixSum = 1, i;

        for (i=1; i<(n+k-1); ++i){
            if (colors[i%n]!=colors[(i-1)%n]) {
                prefixSum++;
            } else {
                if (prefixSum>=k) ans+= prefixSum-k+1;
                prefixSum = 1;
            }
        }
        
        if (prefixSum>=k) ans+= prefixSum-k+1;

        return ans;
    }
};

// class Solution {
// public:
//     int numberOfAlternatingGroups(vector<int>& colors, int k) {
//         int n=colors.size(), ans=0, prefixSum = 1, i;

//         for (i=1; i<n; ++i){
//             if (colors[i]!=colors[i-1]) {
//                 prefixSum++;
//             } else {
//                 if (prefixSum>=k) ans+= prefixSum-k+1;
//                 prefixSum = 1;
//             }
//         }

//         if (colors[0]!=colors[n-1]){
//             prefixSum++;
//             for (i=1; i<(k-1) && colors[i]!=colors[i-1]; ++i) {
//                 prefixSum++;
//             }
//             if (prefixSum>=k) ans+= prefixSum-k+1;
//         } else if(prefixSum>=k){
//             ans+= prefixSum-k+1;            
//         }

//         return ans;
//     }
// };

// class Solution {
// public:
//     int numberOfAlternatingGroups(vector<int>& colors, int k) {
//         int n=colors.size(),i=1, ans=0;
//         vector<int> prefix(n,1);

//         for (; i<n; ++i){
//             if (colors[i]!=colors[i-1]) prefix[i]=prefix[i-1]+1;
//             else if (prefix[i-1]>=k) ans+= prefix[i-1]-k+1;
//         }

//         if (colors[0]!=colors[n-1]){
//             prefix[0] = prefix[n-1]+1;
//             i=1;
//             while (i<(k-1) && prefix[i]!=1){
//                 prefix[i] = prefix[i-1]+1;
//                 i++;
//             }
//             if (prefix[i-1]>=k) ans+= prefix[i-1]-k+1;
//         } else if(prefix[n-1]>=k){
//             ans+= prefix[n-1]-k+1;
            
//         }

//         return ans;
//     }
// };


// class Solution {
// public:
//     int numberOfAlternatingGroups(vector<int>& colors, int k) {
//         int n=colors.size(),i=1, ans=0;
//         vector<int> prefix(n,1);

//         for (; i<n; ++i){
//             if (colors[i]!=colors[i-1]) prefix[i]=prefix[i-1]+1;
//             if (prefix[i]>=k) ans++;
//         }

//         if (colors[0]!=colors[n-1]){
//             prefix[0] = prefix[n-1]+1;
//             if (prefix[0]>=k) ans++;
//             i=1;
//             while (i<(k-1) && prefix[i]!=1){
//                 prefix[i] = prefix[i-1]+1;
//                 if (prefix[i]>=k) ans++;
//                 i++;
//             }
//         }

//         return ans;
//     }
// };

/*
Input: colors = [0,1,0,0,1,0,1], k = 6
Output: 2

[0,1,0,0,1,0,1]
 1,2,3,1,2,3,4
 5,6,7,1,2,3,4       

7-6 +1=2

colors = [0,1,0,1] k = 3 , ans=4
1,2,3,4
5,6,3,4

colors = [0,1,0,1] k = 4 , ans= 4

colors = [0,1,0,1] k = 2 , ans= 4

*/