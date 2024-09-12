#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        int count=0;
        bool valid;
        vector<bool> chars(26, false);
        for (auto& c: allowed) chars[c-97] = true;
        
        for(auto& word: words){
            valid = true;
            for (auto& c: word){
                if (!chars[c-97]){
                    valid = false;
                    break;
                }
            }
            if (valid)  ++count;
        }     

        return count;   
    }
};