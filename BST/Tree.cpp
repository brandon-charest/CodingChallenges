#include "Tree.h"



Tree::Tree() : root(NULL) {};

Tree::~Tree()
{
	destroy_tree(root);
}

int Tree::getMin()
{
	return findMinNode(root);
}

int Tree::getMax()
{
	return 0;
}

bool Tree::isEmpty()
{
	return root == nullptr;
}

bool Tree::contains(int x)
{	
	return findNode(x, root) = NULL ? false : true;
}

void Tree::insert(int data)
{
	root = insert_node(data, root);
}

void Tree::clearTree()
{
}

void Tree::print()
{
}

void Tree::remove(int)
{
}

int Tree::findMinNode(Node *tree)
{
	if (tree == NULL)
	{
		return NULL;
	}

	while (tree->left != NULL)
	{
		tree = tree->left;
	}

	return tree->data;
}

int Tree::findMaxNode(Node *tree)
{
	if (tree == NULL)
	{
		return NULL;
	}

	while (tree->right != NULL)
	{
		tree = tree->right;
	}

	return tree->data;
}

Node *Tree::findNode(int data, Node *node)
{
	if (data = node->data)
	{
		return node;
	}
	else if (data > node->data)
	{
		node->right = insert_node(data, node->right);
	}
	else if (data < node->data)
	{
		node->left = insert_node(data, node->left);
	}
	else
	{
		return NULL;
	}	
}

Node *Tree::insert_node(int data, Node *node)
{
	if (node == NULL)
	{
		node = new Node(data);
	}
	else if (data > node->data)
	{
		node->right = insert_node(data, node->right);
	}
	else
	{
		node->left = insert_node(data, node->left);
	}

	return node;
}

void Tree::destroy_tree(Node *tree)
{
	if (tree != NULL)
	{
		destroy_tree(tree->left);
		destroy_tree(tree->right);

		delete tree;
	}
}

void Tree::preOrder(Node *)
{
}

void Tree::inOrder(Node *)
{
}

void Tree::postOrder(Node *)
{
}
