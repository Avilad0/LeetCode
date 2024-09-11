#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minBitFlips(int start, int goal) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        int flips = 0, diff = start^goal;
        while (diff){
            flips += (diff&1);
            diff>>=1;
        }   
        return flips;   
    }
};

// class Solution {
// public:
//     int minBitFlips(int start, int goal) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

//         int flips = 0, i=1;
//         while (start!=goal){
//             if ( (start&i) != (goal&i) ) {
//                 start ^= i;
//                 ++flips;
//             }
//             i= i<<1;
//         }   
//         return flips;   
//     }
// };




// 101001
// ^
// 110101
// =
// 011100
