/*
 * @lc app=leetcode id=203 lang=cpp
 *
 * [203] Remove Linked List Elements
 */

// @lc code=start
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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *temp;
        ListNode *temp1;

        while(head->val == val){
            head = head->next;
        }
        temp = head;
        if(head->next != NULL)
            temp1 = temp->next;

        while(temp1){
            if(temp1->val == val){
                temp->next = temp1->next;
                temp1= temp1->next;
            }
            temp1 = temp1->next;
            temp = temp->next;
        }
        return head;
    }
};
// @lc code=end

