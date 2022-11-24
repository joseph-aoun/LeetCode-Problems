/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        reverse(head);
        return head;
    }
    
    void reverse(ListNode* head){
        if(!head || !head->next)return;
        int temp = head->val;
        head->val = head->next->val;
        head->next->val = temp;
        reverse(head->next->next);
    }
};