#include<bits/stdc++.h>
using namespace std;

class Solution {
private:
    long long countAtLeastK(string& word, int k){
        int n=word.size(), left = 0, right=0, uniqueVowels=0, consonents = 0;
        long long ans = 0;
        unordered_map<char, int> count = {{'a', 0}, {'e', 0}, {'i', 0}, {'o', 0}, {'u', 0}};
        
        for (right=0;right<n;++right){
            if (count.find(word[right])!=count.end()){
                if (count[word[right]]==0){
                    uniqueVowels++;
                }
                count[word[right]]++;
            } else {
                consonents++;
            }

            while (uniqueVowels==5 && consonents>=k){
                ans += (n-right);
                if (count.find(word[left])!=count.end()){
                    count[word[left]]--;
                    if (count[word[left]]==0){
                        uniqueVowels--;
                    }
                } else {
                    consonents--;
                }
                left++;
            }
        }
        return ans;
    }
public:
    long long countOfSubstrings(string word, int k) {
        return countAtLeastK(word, k) - countAtLeastK(word, k+1);
    }
};

int main(){
    Solution s;
    // cout<<s.countOfSubstrings("ieaouqqieaouqq", 1)<<endl; //3
    // cout<<s.countOfSubstrings("iqeaouqi", 2)<<endl; //3
    cout<<s.countOfSubstrings("aadieuoh", 1)<<endl; //2
    return 0;
}

/*
Input: word = "ieaouqqieaouqq", k = 1
Output: 3
word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".

word ="iqeaouqi"
k = 2
output: 3
*/