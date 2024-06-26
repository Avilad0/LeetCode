#include<bits/stdc++.h>
using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

//this reuses same nodes instead of creating new ones compared to second approach
class Solution {
public:
    TreeNode* balanceBST(TreeNode* root) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        traverse(root);
        return createBalancedBST(0, inorder.size() - 1);
    }

private:
    vector<TreeNode*> inorder;
    void traverse(TreeNode* node) {
        if (node == nullptr) return;
        traverse(node->left);
        inorder.push_back(node);
        traverse(node->right);
    }

    TreeNode* createBalancedBST(int start, int end) {

        if (start > end) return nullptr;
        int mid = start + (end - start) / 2;
        inorder[mid]->left = createBalancedBST(start, mid - 1);
        inorder[mid]->right= createBalancedBST(mid + 1, end);

        return inorder[mid];
    }
};


// class Solution {
// public:
//     TreeNode* balanceBST(TreeNode* root) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

//         vector<int> inorder;
//         traverse(root, inorder);

//         int size = inorder.size();

//         return createBalancedBST(inorder, 0, size - 1);
//     }

// private:
//     void traverse(TreeNode* node, vector<int>& inorder) {
//         if (node == nullptr) return;
//         traverse(node->left, inorder);
//         inorder.push_back(node->val);
//         traverse(node->right, inorder);
//     }

//     TreeNode* createBalancedBST(const vector<int>& inorder, int start,
//                                 int end) {

//         if (start > end) return nullptr;

//         int mid = start + (end - start) / 2;

//         TreeNode* leftSubtree = createBalancedBST(inorder, start, mid - 1);
//         TreeNode* rightSubtree = createBalancedBST(inorder, mid + 1, end);

//         return new TreeNode(inorder[mid], leftSubtree, rightSubtree);
//     }
// };