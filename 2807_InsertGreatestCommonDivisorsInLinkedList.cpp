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


class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        ListNode *node=head;
        int a,b, t;
        while (node->next) {
            a= node->val;
            b= node->next->val;
            while (b!=0){
                t=b;
                b=a%b;
                a=t;
            }
            node->next = new ListNode(a, node->next);
            node= node->next->next;
        }

        return head;
    }
};


// class Solution {
// public:
//     ListNode* insertGreatestCommonDivisors(ListNode* head) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
//         ListNode *node=head;
//         while (node->next) {
//             node->next = new ListNode(gcd(node->val, node->next->val), node->next);
//             node= node->next->next;
//         }

//         return head;
//     }
// };