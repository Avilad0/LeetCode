#include<bits/stdc++.h>
using namespace std;

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {

        ListNode *curr = head, *node = head->next;
        int sum=0;

        while (node){
            
            while ( node->val != 0){
                sum+= node->val;
                node = node->next;
            }
            
            curr->val = sum;
            node = node->next;
            curr->next = node;
            curr=node;
            sum=0;
        }

        return head;
    }
};



// class Solution {
// public:
//     ListNode* mergeNodes(ListNode* head) {

//         ListNode *curr = head, *node = head->next;
//         int sum=0;

//         while (node){
//             if ( node->val == 0){
//                 curr->val = sum;
//                 if (node->next){
//                     curr->next = node;
//                     curr=node;
//                     sum=0;
//                 } else {
//                     curr->next = nullptr;
//                     break;
//                 }
//             } else {
//                 sum+= node->val;
//             }
//             node = node->next;
//         }

//         return head;
//     }
// };