#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        int curr=1;

        for (int i=0;i<n;++i){
            ans.push_back(curr);
            if (curr*10<=n){
                curr*=10;
            } else {
                while (curr%10==9 || curr>=n){
                    curr/=10;
                }
                curr++;
            }
        }
    
        return ans;
    }
};


// class Solution {
// private:
//     vector<int> ans;
//     int n;
//     void dfs(int curr){
//         if (curr>n){
//             return;
//         }

//         ans.push_back(curr);
//         for(int i=0;i<10;++i)   dfs(curr*10 + i);
//     }
// public:
//     vector<int> lexicalOrder(int n) {
//         this->n = n;
//         for(int i=1;i<10;++i)   dfs(i);
//         return ans;
//     }
// };


int main(){
    Solution s;
    vector<int> ans = s.lexicalOrder(13);
    for (auto& x: ans)  cout<<x<<" ";
    return 0;
}