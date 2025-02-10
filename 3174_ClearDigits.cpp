#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string clearDigits(string s) {
        int i=0,j=0,n=s.length();
        for (;i<n;++i){
            s[j]=s[i];
            if (48<=s[i] && s[i]<=57){
                if (j!=0) j--;
            } else {
                ++j;
            }
        }

        s.resize(j);
        return s;
    }
};


int main(){
    Solution s;
    // cout<<s.clearDigits("abc");     //Output: "abc"
    cout<<s.clearDigits("cb34");     //Output: ""

    return 0;
}