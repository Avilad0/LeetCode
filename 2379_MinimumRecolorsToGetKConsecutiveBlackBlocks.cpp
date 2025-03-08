#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int minWhiteConversions = INT_MAX, first = 0, second = 0, n = blocks.size(), whites =0;
        for (;second<n; ++second){
            if (blocks[second]=='W')    whites++;
            if (second-first+1==k){
                if (minWhiteConversions>whites)
                    minWhiteConversions = whites;
                
                if (blocks[first++]=='W')    
                    whites--;
            }
        }

        return minWhiteConversions;
    }
};