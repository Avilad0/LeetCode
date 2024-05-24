#include<bits/stdc++.h>
using namespace std;

class Solution {
private:

    int max_score=0;
    vector<int> letter_freq = vector<int>(26, 0);\

    void check_subsets(vector<string>& words, vector<int>& score, int n, vector<int>& subset_freq, int total_score){

        if (n==-1){
            max_score = max(max_score, total_score);
            return;
        }

        check_subsets(words, score, n-1, subset_freq, total_score);

        bool is_valid = true;
        for ( auto& c :words[n]){
            int ascii = c - 'a';
            subset_freq[ascii]++;
            total_score+=score[ascii];
            if (letter_freq[ascii]<subset_freq[ascii]){
                is_valid = false;
            }
        }

        if (is_valid){
            check_subsets(words, score, n-1, subset_freq, total_score);
        }


        for ( auto& c :words[n]){
            int ascii = c - 'a';
            subset_freq[ascii]--;
            total_score-=score[ascii];
            
        }
        
    }

public:
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        
        for (auto&c: letters){
            letter_freq[c-'a']++;
        }

        vector<int> subset_freq = vector<int>(26, 0);

        check_subsets(words, score, words.size()-1, subset_freq ,0);

        return max_score;
    }
};

int main(){

    Solution s;
    vector<string> words ={"dog","cat","dad","good"};
    vector<char> letters = {'a','a','c','d','d','d','g','o','o'}; 
    vector<int> score ={1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0};
    cout<<s.maxScoreWords( words, letters, score);
    return 0;
}