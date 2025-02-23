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
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        if (preorder.size()==0) return nullptr;

        TreeNode* root = new TreeNode(preorder[0]);
        stack<TreeNode*> stck({root});

        int n=preorder.size(), i=1, j=0;
        for (;i<n;++i){
            TreeNode* node = new TreeNode(preorder[i]);

            if (stck.top()->left == nullptr){
                stck.top()->left = node;
            } else {
                stck.top()->right = node;
            }
            stck.push(node);
            
            while (!stck.empty() && stck.top()->val == postorder[j]) {
                ++j;
                stck.pop();
            }
        }

        return root;
    }
};

int main(){
    Solution s;
    vector<int> preorder = {1,2,4,5,3,6,7}, postorder = {4,5,2,6,7,3,1};
    TreeNode* root = s.constructFromPrePost(preorder, postorder);
    return 0;
}


/*
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

1
2
4 5
*/