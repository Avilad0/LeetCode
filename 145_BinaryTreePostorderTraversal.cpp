#include<bits/stdc++.h>
using namespace std;


//Definition for a binary tree node.
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
    vector<int> postOrder;
    void traverse(TreeNode* node){
        if (node==nullptr) return;

        traverse(node->left);
        traverse(node->right);
        postOrder.push_back(node->val);
    }
public:
    vector<int> postorderTraversal(TreeNode* root) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        traverse(root);
        return postOrder;
    }
};