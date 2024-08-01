#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int countSeniors(vector<string>& details) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        int seniors = 0;
        for (auto& s: details){
            if ( s[11]>'6' || (s[11]=='6' && s[12]>'0' )) seniors++;
        }        

        return seniors;
    }
};