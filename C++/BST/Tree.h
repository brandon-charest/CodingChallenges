#pragma once
#include <iostream>
#include <memory>



class Tree
{	

public:
	Tree();
	~Tree();
	
	void remove(int const &value);
	void isTreeEmpty() const;
	void contains(int const &value) const;
	void findMin() const;
	void findMax() const;
	void insert(int const &value);
	void preOrder() const;
	void inOrder() const;
	void postOrder() const;
	
protected:
	struct Node;
	using pNode = std::unique_ptr<Node>;
	struct Node
	{	
		int data;
		pNode left;
		pNode right;
		Node(int const &value) : data(value) {};

		static pNode from(int const &value)
		{
			return pNode(new Node(value));
		}
	};
	pNode root;

	template<typename T>
	bool isNodeEmpty(T const &node) const;

private:
	bool contains(int const &value, pNode const &node) const;

	int &findMin(pNode const &node) const;
	int &findMax(pNode const &node) const;

	void remove(int const &value, pNode &node);
	void insert(int const &value, pNode &node);
	void preOrder(pNode const &node) const;
	void inOrder(pNode const &node) const;
	void postOrder(pNode const &node) const;	
};

template<typename T>
inline bool Tree::isNodeEmpty(T const &node) const
{
	return node == nullptr;
}
