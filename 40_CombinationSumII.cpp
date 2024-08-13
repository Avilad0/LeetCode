#include<bits/stdc++.h>
using namespace std;

class Solution {
private:
    vector<vector<int>> allCombinations;
    void combinations(vector<int>& candidates, int remainingSum, int index, vector<int>& combination){

        if (remainingSum==0) {
            allCombinations.push_back(combination);
            return;
        }

        for (int i=index; i<candidates.size() && remainingSum>=candidates[i] ; ++i){
            if(i==index || candidates[i]!=candidates[i-1]){
                combination.push_back(candidates[i]);
                combinations(candidates, remainingSum-candidates[i],i+1, combination);
                combination.pop_back();
            }
        }
    }

public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> combination;
        combinations(candidates,target, 0, combination);
        return allCombinations;
    }
};


int main(){
    Solution s;
    vector<int> candidates ={10,1,2,7,6,1,5} ;
    int target = 8;
    for (auto& v: s.combinationSum2(candidates, target)){
        for (auto& i: v){
            cout<<i<<",";
        }
        cout<<endl;
    }
    return 0;
}


//  1   1   2   5   6   7   10
//  