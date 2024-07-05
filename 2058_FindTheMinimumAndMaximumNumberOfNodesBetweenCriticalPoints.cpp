#include<bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        ios_base::sync_with_stdio(false);
        if (!head->next || !head->next->next || !head->next->next->next){
            return {-1,-1};
        }

        
        int i=1, prev = head->val, minDis=INT_MAX, firstCritical=-1, lastCritical=-1;
        
        head=head->next;
        while(head->next){
            if ( (head->val<prev && head->val<head->next->val) || (head->val>prev && head->val>head->next->val)){
                if (firstCritical==-1){
                    firstCritical = i;
                    lastCritical = i;
                } else {
                    if (i - lastCritical < minDis){
                        minDis = i - lastCritical;
                    }
                    lastCritical=i;
                }
            }

            ++i;
            prev = head->val;
            head=head->next;
        }

        if (firstCritical==lastCritical) {
            return {-1,-1}; 
        }

        return {minDis, lastCritical - firstCritical};
    }
};

int main(){
ListNode* head = new ListNode(4);
ListNode* current = head;

current->next = new ListNode(2);
current = current->next;

current->next = new ListNode(4);
current = current->next;

current->next = new ListNode(1);

Solution s;
vector<int> ans = s.nodesBetweenCriticalPoints(head);
cout<<ans[0]<<endl<<ans[1];

return 0;
}