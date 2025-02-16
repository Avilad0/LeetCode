#include<bits/stdc++.h>
using namespace std;

class Solution {
    public:
    vector<int> constructDistancedSequence(int n) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        vector<int> ans(n*2 - 1);
        vector<bool> visited(n+1, false);
        backtrack(n,ans, 0, visited);
        return ans;
    }

    private:
    bool backtrack(int n, vector<int>& ans, int index, vector<bool>& visited){
        if (index == ans.size())    return true;

        if (ans[index]!=0)  return backtrack(n, ans, index+1, visited);

        for (int i=n; i>0;i--){
            if (visited[i]) continue;

            ans[index]=i;
            visited[i] = true;
            
            if (i==1) {
                if (backtrack(n, ans, index+1, visited)){
                    return true;
                }
            } else if ((index+i)<ans.size() && ans[index + i]==0){
                ans[index+i] = i;
                if (backtrack(n, ans, index+1, visited)){
                    return true;
                }
                ans[index+i] =0;
            }

            ans[index]=0;
            visited[i] = false;
        }
        return false;
    }
};


int main(){
    Solution s;
    vector<int> ans = s.constructDistancedSequence(4);
    for (int a:ans){
        cout<<a<<" ";
    }
    return 0;
}



/*
Input: n = 3
Output: [3,1,2,3,2]

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]

n=4
output : [4,2,3,2,4,3,1]

n=6
output : [6,4,2,5,2,4,6,3,5,1,3]

n=7 
output : [7,5,3,6,4,3,5,7,4,6,2,1,2]

n=8
output : [8,6,4,2,7,2,4,6,8,5,3,7,1,3,5] ??


*/