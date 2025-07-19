#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        sort(folder.begin(), folder.end());        
        vector<string> ans;
        
        string curr;
        for (auto& f : folder){
            if (curr.empty() || !f.starts_with(curr)){
                ans.push_back(f);
                curr = f+"/";
            }
        }

        return ans;
    }
};


int main(){
    Solution s;
    vector<string> folder{"/a","/a/b","/c/d","/c/d/e","/c/f"};
    vector<string> ans = s.removeSubfolders(folder);
    for (auto& st : ans)    cout<<st<<" ";
    return 0;
}