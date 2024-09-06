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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        unordered_set<int> numsSet(nums.begin(), nums.end());

        ListNode *dummy = new ListNode(-1, head);
        head=dummy;
        while (head->next != nullptr) {
            if(numsSet.count(head->next->val)!=0){
                head->next=head->next->next;
            } else {
                head=head->next;
            }
        }

        return dummy->next;
    }
};