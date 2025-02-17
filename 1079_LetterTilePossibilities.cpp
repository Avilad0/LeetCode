#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numTilePossibilities(string tiles) {
        vector<int> freq(26,0);
        for (char& c: tiles)    freq[c-65]++;

        backtrack(freq);

        return count;
    }
    
private:
    int count = 0;
    void backtrack(vector<int>& freq){
        for (int i=0; i<26; ++i){
            if (freq[i]>0){
                ++count;
                --freq[i];
                backtrack(freq);
                ++freq[i];
            }
        }
    }
};