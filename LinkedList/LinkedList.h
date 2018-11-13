#pragma once
#include <memory>
#include <iostream>
template <class T>
struct Node
{
	T val;
	Node *next;
	explicit Node(T x) : val(x), next(nullptr){}
};

template <class T>
class LinkedList
{
public:
	LinkedList();
	~LinkedList();

	bool isEmpty();
	void insertBack(T const &x);
	void removeNode(T const &x);
	bool contains(T const &x);
	void removeTail();
	void removeHead();
	void print();
	int size() const;
	void sort();

private:

	
	Node<T> *m_head;
	Node<T> *m_tail;	
	int m_size;

	Node<T>* mergeSort(Node<T> *head);
	Node<T>* merge(Node<T> *node1, Node<T> *node2);
	Node<T>* getMiddle(Node<T> *head);

	static bool isNodeEmpty(Node<T> *node);

};


template <class T>
LinkedList<T>::LinkedList()
{
	m_head = nullptr;
	m_tail = nullptr;
	m_size = 0;
}

template <class T>
LinkedList<T>::~LinkedList()
= default;

template<class T>
bool LinkedList<T>::isEmpty()
{
	return isNodeEmpty(m_head);
}

template <class T>
void LinkedList<T>::insertBack(T const &x)
{
	auto *temp = new Node<T>(x);

	if (isNodeEmpty(m_head))
	{
		m_head = temp;
		m_tail = temp;
	}
	else
	{
		m_tail->next = temp;
		m_tail = temp;
	}

	m_size++;
}

template <class T>
void LinkedList<T>::removeNode(T const& x)
{
	if(isNodeEmpty(m_head) || !contains(x))
	{
		return;
	}


	auto *current = m_head;
	auto *previous = m_head;

	while(!isNodeEmpty(current) && current->val != x)
	{
		previous = current;
		current = current->next;
	}

	if(current->val == x)
	{
		previous->next = nullptr;
		previous->next = current->next;
		current->next = nullptr;
		delete current;

		m_size--;
	}
}

template <class T>
bool LinkedList<T>::contains(T const& x)
{
	if(isNodeEmpty(m_head))
	{
		return false;
	}

	auto *current = m_head;

	while(!isNodeEmpty(current) && current->val != x)
	{
		current = current->next;
	}

	return current->val == x ? true : false;
}

template <class T>
void LinkedList<T>::removeTail()
{
	if (m_tail != nullptr)
	{
		auto *current = m_head;
		auto *previous = m_head;

		while (current->next != nullptr)
		{
			previous = current;
			current = current->next;
		}


		m_tail = previous;
		previous->next = nullptr;

		delete current;
		m_size--;
	}
	else
	{
		std::cout << "There is not tail to remove!" << std::endl;		
	}
}

template <class T>
void LinkedList<T>::removeHead()
{
	if(m_head != nullptr)
	{
		auto *temp = m_head;
		m_head = m_head->next;
		delete temp;

		m_size--;
	}
	else
	{
		std::cout << "There is not head to remove!" << std::endl;
	}
}

template<class T>
void LinkedList<T>::print()
{
	auto *temp = m_head;
	
	while(temp != nullptr)
	{
		std::cout << temp->val << " -> ";
		temp = temp->next;
	}
	std::cout << std::endl;
	delete temp;
}

template<class T>
int LinkedList<T>::size() const
{
	return m_size;
}

template<class T>
void LinkedList<T>::sort()
{
	m_head = mergeSort(m_head);
}

template <class T>
Node<T>* LinkedList<T>::mergeSort(Node<T> *head)
{
	if(head == nullptr || head->next == nullptr)
	{
		return head;
	}

	Node<T> *middleNode = getMiddle(head);
	Node<T> *half = middleNode->next;
	middleNode->next = nullptr;


	return merge(mergeSort(head), mergeSort(half));

}

template <class T>
Node<T>* LinkedList<T>::merge(Node<T> *node1, Node<T> *node2)
{
	Node<T> *temp;

	if(node1 == nullptr)
	{
		return node2;
	}

	if(node2 == nullptr)
	{
		return node1;
	}


	if(node1->val < node2->val)
	{
		temp = node1;
		temp->next = merge(node1->next, node2);
	}
	else
	{
		temp = node2;
		temp->next = merge(node1, node2->next);
	}

	return temp;
}

template <class T>
Node<T>* LinkedList<T>::getMiddle(Node<T> *head)
{
	if(head == nullptr)
	{
		return head;
	}

	Node<T> *slow = head;
	Node<T> *fast = head;

	while(fast->next != nullptr && fast->next->next != nullptr)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return slow;
}

template <class T>
bool LinkedList<T>::isNodeEmpty(Node<T>* node)
{
	return node == nullptr;
}



