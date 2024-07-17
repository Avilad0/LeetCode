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
private:
    vector<TreeNode*> forest;
    unordered_set<int> toDeleteSet;
    TreeNode* dfs(TreeNode* node){
        if (node == nullptr){
            return node;
        }

        node->left = dfs(node->left);
        node->right = dfs(node->right);

        if (toDeleteSet.find(node->val) != toDeleteSet.end()){
            if (node->left != nullptr) forest.push_back(node->left);
            if (node->right!= nullptr) forest.push_back(node->right);

            return nullptr;
        }
        return node;
    }

public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        toDeleteSet = unordered_set<int>(to_delete.begin(), to_delete.end());
        TreeNode* node = dfs(root);
        if (node!=nullptr) forest.push_back(node);

        return forest;
    }
};