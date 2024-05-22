#include<bits/stdc++.h>
using namespace std;

class Solution {
private:
    int l;
    vector<vector<string>> ans;
    bool is_palindrome(string& s, int left, int right){
        while(left<right){
            if(s[left++] != s[right--]){
                return false;
            }
        }
        return true;
    }

    void backtrack(string& s, int start, vector<string>& path){
        if (start==l){
            ans.push_back(path);
            return;
        }

        for(int end=start+1;end<=l;end++){

            if(is_palindrome(s, start, end-1)){
                path.push_back(s.substr(start, end-start));
                backtrack(s, end, path);
                path.pop_back();
            }
        }
    }

public:
    vector<vector<string>> partition(string s) {
        l = s.length();
        vector<string> path;
        backtrack(s,0,path);
        return ans;
    }
};