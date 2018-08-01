#pragma once
#include <iostream>
struct Node
{
	int data;
	Node *left;
	Node *right;	
	Node(int x) : data(x), left(nullptr), right(nullptr) {};
};

class Tree
{	
public:
	Tree();
	~Tree();
	

	int getMin();
	int getMax();

	bool isEmpty();
	bool contains(int);

	void insert(int);
	void clearTree();
	void print();
	void remove(int);
	


private:
	Node *root;

	int findMinNode(Node*);
	int findMaxNode(Node*);
	Node *findNode(int, Node*);

	Node *insert_node(int, Node*);
	void destroy_tree(Node*);
	void preOrder(Node*);
	void inOrder(Node*);
	void postOrder(Node*);
};

