#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int strangePrinter(string s) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        //remove duplicate
        int i=0,j=0, n=s.size();
        while (j<n){
            s[i]=s[j++];
            while(j<n && s[j]==s[i]) ++j;
            ++i;
        }
        s = s.substr(0, i);

        memo = vector<vector<int>>(i, vector<int>(i, -1));

        return checkSubString(s, 0, i-1);
    }

private:

    vector<vector<int>> memo;

    int checkSubString(string& s, int left, int right){
        
        if (left>right) return 0;
        if (memo[left][right] != -1) return memo[left][right];

        int minSteps = 1 + checkSubString(s, left+1, right);

        for (int i= left+1; i<=right; ++i){
            if (s[left]==s[i]) minSteps = min(minSteps, checkSubString(s, left, i-1) + checkSubString(s, i+1, right));
        }

        memo[left][right] = minSteps;

        return minSteps;
    }
};

int main(){
    Solution s;
    cout<<s.strangePrinter("aaabbbaaa");
    return 0;
}

/*
Input: s = "aba"
Output: 2
1) aaa
2) aba

s = "aabbbccaaa"
ans =3
1) aaaaaaaaaa
2) aabbbaaaaa
3) aabbbccaaa

s = "abcba"
ans =3
1) aaaaa
2) abbba
3) abcba

s = "abcab"
ans =4
1) aaaa
2) abaa
3) abaab
4) abcab
*/