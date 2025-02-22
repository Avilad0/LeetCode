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
    TreeNode* recoverFromPreorder(string traversal) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        stack<TreeNode*> stck;
        int index = 0, n= traversal.size(), depth, val;
        
        while(index<n){
            depth = 0;
            while((index+depth)<n && traversal[index+depth]=='-') ++depth;

            while(depth<stck.size())    stck.pop();

            index+=depth;
            val = 0;
            while(index<n && traversal[index]!='-')     val = val*10 + (traversal[index++] - '0');
            
            TreeNode* node = new TreeNode(val);
            if (stck.size()>0){
                if(stck.top()->left==nullptr){
                    stck.top()->left = node;
                } else {
                    stck.top()->right = node;
                }
            }
            stck.push(node);
        }

        while (stck.size()>1)   stck.pop();

        return stck.top();
    }
};

// class Solution {
// private:
//     int index = 0;
//     int dfs(TreeNode* node, string& traversal, int depth) {
//         if (index==traversal.size())  return -1;

//         int i=index;
//         while (i<traversal.size() && traversal[i]!='-')   ++i;
//         int val = stoi(traversal.substr(index, i-index));
//         node->val = val;
//         index = i;

//         while (i<traversal.size() && traversal[i]=='-') i++;
//         int newDepth=i-index;
//         index = i;

//         if (depth+1 == newDepth){
//             node->left = new TreeNode();
//             int nextDepth = dfs(node->left, traversal, newDepth);
//             if (nextDepth == newDepth){
//                 node->right = new TreeNode();
//                 return dfs(node->right, traversal, nextDepth);
//             } else {
//                 return nextDepth;
//             }
//         } else {
//             return newDepth;
//         }
//     }
// public:
//     TreeNode* recoverFromPreorder(string traversal) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

//         if (traversal.size()<1) return nullptr;
        
//         TreeNode* root = new TreeNode();
//         dfs(root, traversal, 0);
//         return root;
//     }
// };


int main(){
    Solution s;
    cout<<s.recoverFromPreorder("1-2--3---4-5--6---7");
    return 0;
}