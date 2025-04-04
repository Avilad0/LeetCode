#include<bits/stdc++.h>
using namespace std;

/**
 * Definition for a binary tree node.
 */
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
    int maxDepth = 0;
    TreeNode* lca = nullptr;

    int dfs(TreeNode* node, int depth){
        if (node == nullptr){
            return -1;
        }
        if (node->left == nullptr && node->right == nullptr){
            if (depth > maxDepth){
                maxDepth = depth;
                lca = node;
            } 
            return depth;
        }
        
        int leftMaxDepth = dfs(node->left, depth+1);
        int rightMaxDepth = dfs(node->right, depth+1);

        if (maxDepth == leftMaxDepth && maxDepth == rightMaxDepth){
            lca = node;
        }

        return max(leftMaxDepth, rightMaxDepth);
    }

public:
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        dfs(root, 1);

        return lca;
    }
};