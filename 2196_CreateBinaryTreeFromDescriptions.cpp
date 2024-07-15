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


// [parent, child, isLeft]
class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        unordered_map<int, TreeNode*> nodes;
        unordered_set<int> values;

        for (auto& desc : descriptions){

            if (nodes.find(desc[0])==nodes.end()) nodes[desc[0]] = new TreeNode(desc[0]);
            if (nodes.find(desc[1])==nodes.end()) nodes[desc[1]] = new TreeNode(desc[1]);
        
            if (desc[2]==1) nodes[desc[0]]->left = nodes[desc[1]];
            else            nodes[desc[0]]->right= nodes[desc[1]];

            values.insert(desc[1]);
        }

        for (auto& desc : descriptions){
            if (values.find(desc[0]) == values.end()){
                return nodes[desc[0]];
            }
        }

        return nullptr;
    }
};


int main(int argc, char const *argv[])
{
    Solution s;
    vector<vector<int>> descriptions = { {20,15,1},{20,17,0},{50,20,1},{50,80,0},{80,19,1}};
    TreeNode *root = s.createBinaryTree(descriptions);
    return 0;
}
