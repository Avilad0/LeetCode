#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string makeFancyString(string s) {
        string ans = s.substr(0,2);
        int n = s.length();
        for (int i=2; i<n; ++i){
            if (s[i]!=s[i-1] || s[i]!=s[i-2])   ans += s[i];
        }        
        return ans;
    }
};