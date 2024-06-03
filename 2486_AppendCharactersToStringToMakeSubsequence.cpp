#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int appendCharacters(string s, string t) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        int n_s = s.length(), n_t= t.length();
        int i,j=0;
        for (i=0;i<n_s;++i){
            if (s[i]==t[j]){
                j++;
                if (j==n_t){
                    return 0;
                }
            }
        }
        return n_t - j;
    }
};