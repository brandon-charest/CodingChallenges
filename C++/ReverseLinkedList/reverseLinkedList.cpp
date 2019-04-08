/*206. Reverse Linked List
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
 */

#include <iostream>


struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
	
};




ListNode* reverseList(ListNode* head) 
{
	if(head == nullptr)
	{
		return head;
	}

	ListNode* prev = nullptr;
	ListNode* next = nullptr;
	ListNode* current = head;

	while(current != nullptr)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return head = prev;
}

int main()
{	
	return 0;
}