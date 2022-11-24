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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* head3 = new ListNode();
        merge(list1, list2, head3);
        return head3->next;
    }
    void merge(ListNode* head1, ListNode* head2, ListNode* head3){
        if(!head1) {head3->next = head2; return;}
        if(!head2) {head3->next = head1; return;}
        
        if(head1->val < head2->val){
            head3->next = new ListNode(head1->val);
            head1 = head1->next;
        }
        else{
            head3->next = new ListNode(head2->val);
            head2 = head2->next;
        }
        
        head3 = head3->next;
        merge(head1, head2, head3);
    }
};