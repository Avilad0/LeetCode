#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        if (chalk[0]>k) return 0;

        int i,n=chalk.size();
        for (i=1;i<n;++i){
            chalk[i]+=chalk[i-1];
            if (chalk[i]>k) return i;
        }

        k%=chalk[n-1];

        for (i=0;i<n;++i){
            if (chalk[i]>k) return i;   
        }

        return -1; //impossible
    }
};