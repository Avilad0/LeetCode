#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char,int> count;
        for (char& c: s){
            count[c]++;
        }

        int odds = 0;
        for (auto& [c,n]: count){
            if(n%2==1){
                odds++;
            }
        }

        return s.length() - odds + (odds==0?0:1) ;
    }
};