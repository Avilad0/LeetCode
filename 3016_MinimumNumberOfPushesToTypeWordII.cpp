#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumPushes(string word) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        vector<int> freq(26,0);        
        for (char c: word) ++freq[c-'a'];

        sort(freq.begin(), freq.end(), greater<>());
        // alternate for descending sorting
        // sort(frequency.rbegin(), frequency.rend());

        int ans =0, keyPress=1, i=0;
        while (i<26 && freq[i]!=0){
            ans += keyPress*freq[i];
            
            if ((++i)%8 == 0)   ++keyPress;
        }

        return ans;
    }
};