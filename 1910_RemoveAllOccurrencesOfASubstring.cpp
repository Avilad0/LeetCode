#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string removeOccurrences(string s, string part) {
        int n= s.length(), m=part.length(), i=0,j=0,t;
        if (m>n)    return s;

        for(;i<n;++i){
            if (s[i]==part[m-1]){
                t=1;
                while (t<m && (j-t)>=0 && s[j-t]==part[m-1-t]) t++;
                if (t==m) {
                    j=j-m+1;
                } else{
                    s[j++]=s[i];    
                }
            } else {
                s[j++]=s[i];
            }
        }

        s.resize(j);
        return s;
    }
};

int main(){
    Solution s;
    cout<<s.removeOccurrences("daabcbaabcbc", "abc");   //Output: "dab"
    return 0;
}