#include<bits/stdc++.h>
using namespace std;

class Solution {
private:
    vector<string> ans;
    void findSentences(string& s, int n_s, vector<string>& wordDict, int n, vector<int>& n_w, vector<vector<int>>& indexes_s, int i, string sentence ){
        if (i==n_s){
            sentence.pop_back();
            ans.push_back(sentence);
            return;
        }

        for (auto& i_s: indexes_s[i]){
            findSentences(s, n_s, wordDict, n, n_w, indexes_s, i+ n_w[i_s], sentence + wordDict[i_s] + " ");
        }

    }


public:

    vector<string> wordBreak(string s, vector<string>& wordDict) {
        int n = wordDict.size();
        
        vector<int> n_w;
        for (auto& w: wordDict){
            n_w.push_back(w.length());
        }


        vector<vector<int>> indexes = vector<vector<int>>(n);

        int n_s =s.length();
        vector<vector<int>> indexes_s = vector<vector<int>>(n_s);

        int t;
        for (int i =0; i<n; i++){
            t=-1;
            while(true){
                t=s.find(wordDict[i],t+1);
                if (t==string::npos){
                    break;
                }
                indexes_s[t].push_back(i);
            }
        }

        findSentences(s, n_s, wordDict, n, n_w, indexes_s, 0, "" );
        return ans;
    }
};

// int main(){
//     Solution s;
//     vector<string> words = {"cat","cats","and","sand","dog"};
//     s.wordBreak("catsanddog", words);
//     for (auto& c: s.ans){
//         cout<<c<<endl;
//     }
//     return 0;
// }