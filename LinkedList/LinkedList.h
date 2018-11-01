#pragma once
#include <memory>
#include <iostream>
template <class T>
struct Node
{
	T val;
	Node *next;
	explicit Node(T x) : val(x), next(nullptr) {};
};

template <class T>
class LinkedList
{
public:
	LinkedList();
	~LinkedList();

	bool isEmpty();
	void insertBack(T const &x);
	void remove(T const &x);
	void print();
	int size();
	void sort();

private:

	
	Node<T> *m_head;
	Node<T> *m_tail;
	

	static bool isNodeEmpty(Node<T> *node);
	void insertBack(T const &x, Node<T> *node);
	void remove(T const &x, Node<T> &node);

};


template <class T>
LinkedList<T>::LinkedList()
{
	m_head = nullptr;
	m_tail = nullptr;
	m_temp = nullptr;
}

template <class T>
LinkedList<T>::~LinkedList()
= default;

template<class T>
bool LinkedList<T>::isEmpty()
{
	return isNodeEmpty(m_head);
}

template<class T>
void LinkedList<T>::insertBack(T const &x)
{
	insertBack(x, m_head);
}

template<class T>
void LinkedList<T>::remove(T const &x)
{
	remove(x, m_head);
}

template<class T>
void LinkedList<T>::print()
{
}

template<class T>
int LinkedList<T>::size()
{
	return 0;
}

template<class T>
void LinkedList<T>::sort()
{
}

template <class T>
bool LinkedList<T>::isNodeEmpty(Node<T>* node)
{
	return node == nullptr;
}

template <class T>
void LinkedList<T>::insertBack(T const &x, Node<T> *node)
{
	auto *temp = new Node<T>(x);

	if(isNodeEmpty(m_head))
	{
		m_head = temp;
		m_tail = temp;
	}
	else
	{
		m_tail->next = temp;
		m_tail = temp;
	}

	delete temp;
}

template <class T>
void LinkedList<T>::remove(T const &x, Node<T> &node)
{
}