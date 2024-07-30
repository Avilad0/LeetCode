#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int minimumDeletions(string s) {
        int n=s.size(), i, countA=0, countB=0, minimumDeletions;
        vector<int> ascCountB(n), dscCountA(n);

        for (i=0; i<n; ++i){
            ascCountB[i] = countB;
            if (s[i]=='b') ascCountB[i] = countB++;

            dscCountA[n-i-1] = countA;
            if (s[n-i-1]=='a') countA++;
        }

        minimumDeletions = ascCountB[0]+dscCountA[0];
        for (i=1;i<n;++i){
            minimumDeletions = min(minimumDeletions, ascCountB[i]+dscCountA[i]);
        }

        return minimumDeletions;
    }
};


