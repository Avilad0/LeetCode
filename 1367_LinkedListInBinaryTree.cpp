#include<bits/stdc++.h>
using namespace std;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

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
    bool dfs(TreeNode* treeNode, ListNode* listNode){
        
        if (listNode==nullptr) return true;
        if (treeNode==nullptr || treeNode->val != listNode->val) return false;

        return dfs(treeNode->left, listNode->next) || dfs(treeNode->right, listNode->next);
    }

public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        if(!root) return false;
        
        if (dfs(root, head)) return true;

        return isSubPath(head, root->left) || isSubPath(head, root->right); 
    }
};

// class Solution {
// private:
//     ListNode* originalHead;
//     bool isSub(TreeNode* treeNode, ListNode* listNode){
        
//         if (listNode==nullptr) return true;
//         if (treeNode==nullptr) return false;

//         if (treeNode->val == listNode->val && (isSub(treeNode->left, listNode->next) || isSub(treeNode->right, listNode->next))) return true;
        
//         // if (treeNode->val == originalHead->val)  return isSub(treeNode->left, originalHead->next) || isSub(treeNode->right, originalHead->next);
        
//         return isSub(treeNode->left, originalHead) || isSub(treeNode->right, originalHead);
//     }

// public:
//     bool isSubPath(ListNode* head, TreeNode* root) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
//         originalHead = head;
//         return isSub(root, head);
//     }
// };