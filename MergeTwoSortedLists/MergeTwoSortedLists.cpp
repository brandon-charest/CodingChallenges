/* 21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4*/

#include <vector>
struct ListNode
{
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(nullptr){}
};


void addNode(ListNode *head,int x)
{
	ListNode *temp = new ListNode(x);


	while (head)
	{
		if (head->next == nullptr)
		{
			head->next = temp;
			return;
		}
		head = head->next;
	}

}


ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
{
	if (l1 == nullptr)
	{
		return l2;
	}
	else if (l2 == nullptr)
	{
		return l1;
	}


	ListNode *temp = NULL;
	

	if (l1->val < l2->val)
	{
		temp = l1;
		l1 = l1->next;
	}
	else
	{
		temp = l2;
		l2 = l2->next;
	}

	ListNode *p = temp;
	while (l1 && l2)
	{
		if (l1->val < l2->val)
		{
			p->next = l1;
			l1 = l1->next;
		}
		else
		{
			p->next = l2;
			l2 = l2->next;
		}
		p = p->next;
	}
	

	if (l1)
	{
		p->next = l1;
	}
	else
	{
		p->next = l2;
	}

	return temp;
}

int main()
{
	ListNode *l1 = new ListNode(1);
	addNode(l1, 2);
	addNode(l1, 4);

	ListNode *l2 = new ListNode(1);
	addNode(l2, 3);
	addNode(l2, 4);
	
	ListNode *l3 = mergeTwoLists(l1, l2);
	


	return 0;
}

