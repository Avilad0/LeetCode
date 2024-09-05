#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        int m = rolls.size(), totalRollsM = accumulate(rolls.begin(), rolls.end(), 0), totalRollsN= mean*(n+m) - totalRollsM;
        double mMean=double(totalRollsM)/m, nMean= double(totalRollsN)/n;

        if (nMean>6.0 || nMean<1.0) return {};

        int extras = totalRollsN%n, newMean = (totalRollsN-extras)/n, i=0;
        vector<int> nRolls;
        for (i=0;i<extras;++i) nRolls.push_back(newMean + 1);
        for (;i<n;++i) nRolls.push_back(newMean);

        return nRolls;
    }
};

int main(){
    Solution s;
    // vector<int> rolls = {3,2,4,3};
    // int mean=4,n=2;
    // vector<int> rolls = {1,5,6};
    // int mean=3,n=4;
    
    vector<int> rolls = {6,1,5,2};
    int mean=4,n=4;
    
    for (auto& x: s.missingRolls(rolls, mean, n)){
        cout<<x<<" ";
    }
    return 0;
}


/*
Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]

3+2+4+3 /4 = 12/4 = 3
mean = 4

3*m + x*n / m+n = 4
12 + 2x/6 = 4
2x = 24 - 12
x=6

-----------------

Input: rolls = [1,2,3,4], mean = 6, n = 4
Output: []

1+2+3+4 = 10
mMean = 10/4 = 2.5
nMean = (6*8 - 10)/4 = (38)/4 = 9.5
*/