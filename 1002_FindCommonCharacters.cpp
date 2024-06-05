#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> commonChars(vector<string>& words) {

        vector<int> common_freq(26,101); //max freq is 100 as per question.
        int i;

        for (auto& w : words){
            vector<int> word_freq(26,0);
            
            for (auto& c:w){
                word_freq[c-'a']++;
            }

            for ( i=0;i<26;++i){
                if (common_freq[i]>word_freq[i]){
                    common_freq[i]=word_freq[i];
                }
            }
        }

        vector<string> ans;
        for (i=0;i<26;++i){
            if(common_freq[i]!=101){
                ans.insert(ans.end(),common_freq[i], string()+char('a'+i));
            }
        }

        return ans;
    }
};

int main(){
    Solution s;
    vector<string> words = {"bella","label","roller"};
    for (string c: s.commonChars(words)){
        cout<<c;
    }
    return 0;
}