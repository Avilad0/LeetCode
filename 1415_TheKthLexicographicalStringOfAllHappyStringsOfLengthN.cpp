#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string getHappyString(int n, int k) {
        if (k>3*(1<<(n-1))) return "";
        
        string ans(n, 'x'); 
        unordered_map<char,char> first = {{'a','b'}, {'b','a'}, {'c','a'}}, second = {{'a','c'}, {'b','c'}, {'c','b'}};

        int onePart = 1<<(n-1);
        if (k<=onePart){
            ans[0]='a';
            k-=1;
        } else if (k<=(2*onePart)){
            ans[0]='b';
            k= k - 1 - onePart;
        } else {
            ans[0]='c';
            k= k - 1 - 2*onePart;
        }

        for(int i=1; i<n; ++i){
            onePart>>=1;
            if (k<onePart){
                ans[i] = first[ans[i-1]];
            } else {
                ans[i] = second[ans[i-1]];
                k-=onePart;
            }
        }

        return ans;
    }
};


/*
n=1
a
b
c

n=2
ab
ac
ba
bc
ca
cb

n=3
aba
abc
aca
acb
bab
bac
bca
bcb
cab
cac
cba
cbc

n=4
abab
abac
abca
abcb
acab
acac
acba
acbc
baba
babc
baca
bacb
bcab
bcac
bcba
bcbc
caba
cabc
caca
cacb
cbab
cbac
cbca
cbcb

*/