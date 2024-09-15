#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTheLongestSubstring(string s) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        vector<int> bitmaskIndexes(32, -2);
        bitmaskIndexes[0]=-1;
        int bitmask=0, n = s.size(), i=0, maxLength = 0;

        for(;i<n;++i){

            switch (s[i]) {
                case 'a': 
                    bitmask ^= 1;
                    break;
                case 'e':
                    bitmask ^= 2;
                    break;
                case 'i':
                    bitmask ^= 4;
                    break;
                case 'o':
                    bitmask ^= 8;
                    break;
                case 'u':
                    bitmask ^= 16;
            }

            if (bitmaskIndexes[bitmask] == -2){
                bitmaskIndexes[bitmask] = i;
            }
            maxLength = max(maxLength, i - bitmaskIndexes[bitmask]);
        }

        return maxLength;
    }
};


/*

eleetminicoworoep

_ = 00000
e = 00010
l = 00010
e = 00000
e = 00010
t = 00010
m = 00010
i = 00110
n = 00110
i = 00010
c = 00010
o = 01010
w = 01010
o = 00010
r = 00010
o = 01010
e = 01000
p = 01000

*/


// 11111
// 1+2+4+8+16 = 31