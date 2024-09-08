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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        int n = 0;
        ListNode *node = head, *prev;
        while (node){
            node=node->next;
            ++n;
        }

        int splitSize = n/k, extras = n%k, currsize;
        node=head;
        vector<ListNode*> splitHeads(k,nullptr);
        for (int i=0;i<k;++i){

            splitHeads[i] = node;

            currsize = splitSize + ((extras--)>0) - 1;
            for(int j=0;j<currsize;++j) node=node->next;

            if (node){
                prev = node;
                node=node->next;
                prev->next = nullptr;
            } else {
                break;
            }
        }

        return splitHeads;     
    }
};


int main(){
    // Input: head = [1,2,3], k = 5
    // Output: [[1],[2],[3],[],[]]

    ListNode *head = new ListNode(1,new ListNode(2,new ListNode(3)));
    Solution s;
    s.splitListToParts(head, 5);
    return 0;
}