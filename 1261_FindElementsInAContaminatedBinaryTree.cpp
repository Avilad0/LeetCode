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

class FindElements {
private:
    TreeNode* root;
    void dfs(TreeNode* node, int val){
        if (node == nullptr)    return;

        node->val = val;

        dfs(node->left,  val*2 + 1);
        dfs(node->right, val*2 + 2);
    }
public:
    FindElements(TreeNode* root) {
        this->root = root;
        dfs(root, 0);
    }
    
    bool find(int target) {        
        int newTarget = target+1, bits = log2(newTarget)-1;
        TreeNode* node = root;
        while (node && bits>=0){
            if (((newTarget>>bits) & 1) == 0){
                node = node->left;
            } else {
                node = node->right;
            }
            --bits;
        }
        return node != nullptr;
    }
};
    
/*
class FindElements {
private:
    unordered_set<int> nums;
    void dfs(TreeNode* node){
        nums.insert(node->val);
        if (node->left != nullptr){
            node->left->val = node->val *2 +1;
            dfs(node->left);
        }
        if (node->right != nullptr){
            node->right->val = node->val *2 +2;
            dfs(node->right);
        }
    }
public:
    FindElements(TreeNode* root) {
        if (root !=nullptr){
            root->val= 0;
            dfs(root);
        }
    }
    
    bool find(int target) {
        return nums.find(target) != nums.end();
    }
};
*/


/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */

int main(){
    TreeNode* root = new TreeNode(0);
    TreeNode* node1 = new TreeNode(-1);
    root->right = node1;
    FindElements* obj = new FindElements(root);
    cout<<obj->find(1);
    cout<<obj->find(2);
    return 0;
}



/*
               0
      1                2
  3       4        5       6
7   8   9   10  11  12  13  14

with binary
               0
      1                    10
  11        100      101        110
111 1000 1001 1010 1011 1100 1101 1110

with binary+1
               1
      10                   11
  100       101        110       111
1000 1001 1010 1011 1100 1101 1110  1111

2**1  -2
2**1 -1     2**2  -2
2**2 -1     2**3  -2
2**3 -1     2**4  -2
*/