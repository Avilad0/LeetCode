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
    int dfs(TreeNode* node, int sum){
        if (node==nullptr){
            return sum;
        }
        node->val += dfs(node->right, sum);
        return dfs(node->left, node->val);
    }
public:
    TreeNode* bstToGst(TreeNode* root) {
        dfs(root, 0);
        return root;
    }
};

int main(){
    Solution s;
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(1);
    root->right = new TreeNode(6);
    root->left->left = new TreeNode(0);
    root->left->right = new TreeNode(2);
    root->right->left = new TreeNode(5);
    root->right->right = new TreeNode(7);
    root->left->right->right = new TreeNode(3);
    root->right->right->right = new TreeNode(8);
    cout<<s.bstToGst(root);
    return 0;
}


//             4
//     1               6
// 0       2       5      7   
//           3              8




//             5
//     2               12
// 1       3       10      15   


//             5
//     2               12
// 1       3       10      15   
