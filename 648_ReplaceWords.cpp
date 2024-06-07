#include<bits/stdc++.h>
using namespace std;


// this can also be done by TrieNode, i.e. convert each dictionary word into tree structure.

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {

        unordered_set<string> dict(dictionary.begin(), dictionary.end());
        map<string, string> derivativeToRoot;

        istringstream stream(sentence);
        string ans, word, t;
        int i;  
        bool found;

        while (getline(stream, word, ' ')) {
            if (derivativeToRoot.find(word)!= derivativeToRoot.end()){
                ans.append(derivativeToRoot[word]+' ');
                continue;
            }

            t = "";
            found= false;
            for (i=0;i<word.length();++i){
                t+=word[i];
                if(dict.find(t)!= dict.end()){
                    found=true;
                    break;
                }
            }

            if (!found){
                t = word;
            }
            ans.append(t+' ');
            derivativeToRoot[word]= t;
        }

        ans.pop_back();
        return ans;
    }
};


int main(){
    vector<string> dictionary ={"cat","bat","rat"};
    string sentence = "the cattle was rattled by the battery";
    Solution s;
    cout<< s.replaceWords(dictionary, sentence);
    return 0;
}