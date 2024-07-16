#include<bits/stdc++.h>
using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    string getDirections(TreeNode* root, int startValue, int destValue) {

        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        startVal = startValue;
        destVal = destValue;
        string path = "";
        dfs(root, path);

        int i = 0;
        while (i<startPath.length() && i<destPath.length() && startPath[i]==destPath[i]) ++i;

        string ans(startPath.length() - i ,'U');

        return ans + destPath.substr(i);
    }

private:
    string startPath, destPath;
    int startVal, destVal, count=0;

    void dfs(TreeNode* node, string& path){
        if (node == nullptr || count==2){
            return;
        }

        if (startVal == node->val){
            startPath = path;
            count++;
        } else if (destVal == node->val){
            destPath = path;
            count++;
        }

        path.push_back('L');
        dfs(node->left, path);
        path.pop_back();

        path.push_back('R');
        dfs(node->right, path);
        path.pop_back();

    }
};