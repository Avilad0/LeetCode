#include<bits/stdc++.h>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};


// This is equally good compared with iterative approach but iterative is better when dealing with large set of numbers as recursive call stack can be limited.
class Solution {
private:
    vector<int> postOrder;
    void traverse(Node* node){
        if (node==nullptr) return;

        for (auto& child: node->children){
            traverse(child);
        }
        postOrder.push_back(node->val);
    }
public:
    vector<int> postorder(Node* root) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        traverse(root);
        return postOrder;
    }
};